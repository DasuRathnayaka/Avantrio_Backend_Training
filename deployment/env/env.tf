terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.62.0"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "project"
  region  = "us-east-2"
}

data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-ebs"]
  }
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "project-vpc-prod"
  cidr = "10.1.0.0/16"

  azs             = ["us-east-2a", "us-east-2b", "us-east-2c"]
  private_subnets = ["10.1.1.0/24", "10.1.2.0/24", "10.1.3.0/24"]
  public_subnets  = ["10.1.101.0/24", "10.1.102.0/24", "10.1.103.0/24"]

  enable_nat_gateway = false
  enable_vpn_gateway = false

  # single_nat_gateway = true

  enable_dns_hostnames = true

  tags = {
    Terraform = "true"
    Environment = "prod"
    
  }
}

resource "aws_security_group" "rds_sg" {
  name        = "project-dev-rds-sg"
  description = "Allow DB access"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description      = "DB port"
    from_port        = 5432
    to_port          = 5432
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "project-dev-rds-sg"
  }
}

module "db" {
  source  = "terraform-aws-modules/rds/aws"

  identifier = "project-prod-rds"

  engine            = "postgres"
  engine_version    = "13.4"
  instance_class    = "db.t3.small"
  allocated_storage = 20

  db_name  = "project"
  username = "project"
  port     = "5432"
  password = "PASSWORD"

  multi_az = false
  iam_database_authentication_enabled = true

  maintenance_window = "Mon:00:00-Mon:03:00"
  backup_window      = "03:00-06:00"

  create_monitoring_role = false
  
  tags = {
    Owner       = "user"
    Environment = "prod"
  }
 
  create_db_subnet_group = true
  subnet_ids             = module.vpc.private_subnets
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  family = "postgres13"

  # Database Deletion Protection
  deletion_protection = true

  apply_immediately = true

  storage_encrypted = false
}

resource "aws_security_group" "app_instance_sg" {
  name        = "project-prod-server-sg"
  description = "Allow SSH/TCP and Web"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description      = "Django port"
    from_port        = 8000
    to_port          = 8000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "SSH port"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "project-prod-server-sg"
  }
}

resource "aws_instance" "app_server" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.medium"
  key_name      = "project-prod"

  root_block_device {
    volume_size = 30
  }

  user_data = <<-EOF
    #!/bin/bash
    set -ex
    sudo yum update -y
    sudo yum install docker -y
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    udo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo systemctl enable docker.service
    sudo systemctl enable containerd.service
    sudo mkdir /project
    sudo chown -R ec2-user:ec2-user /project
  EOF

  
  vpc_security_group_ids = [aws_security_group.app_instance_sg.id]
  subnet_id = module.vpc.public_subnets[0]

  tags = {
    Name = "project-prod-instance"
  }
}

# create load balancer
resource "aws_security_group" "app_load_balancer_sg" {
  name        = "project-prod-app-lb-sg"
  description = "Allow SSH/TCP and Web"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description      = "HTTP port"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "HTTPS port"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "project-prod-app-lb-sg"
  }
}

resource "aws_lb" "app_load_balancer" {
  name = "project-prod-lb"
  internal = false
  load_balancer_type = "application"
  security_groups = [aws_security_group.app_load_balancer_sg.id]
  subnets = [for subnet in module.vpc.public_subnets : subnet]

  enable_deletion_protection = true
  
  tags = {
    Environment = "prod"
  }
}

# create target group
resource "aws_lb_target_group" "app_lb_target_group" {
  name = "project-prod-app-lb-tg"
  target_type = "instance"
  port = 80
  protocol = "HTTP"
  vpc_id = module.vpc.vpc_id
  health_check {
    healthy_threshold = "3"
    interval = "30"
    unhealthy_threshold = "3"
    timeout = "20"
    path = "/api"
    port = "8000"
  }
}

# attach
resource "aws_lb_target_group_attachment" "app_lb_target_group_attachment" {
  target_group_arn = aws_lb_target_group.app_lb_target_group.arn
  target_id = aws_instance.app_server.id
  port = 8000
}
