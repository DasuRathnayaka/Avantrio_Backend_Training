# Deployment

Deployments are managed using Terraform. Each environment should have the following,

1. Terraform script (env.tf)
2. Docker compose file (docker-compose.yml)
3. Environment variables (common.env)
4. Docker pull script
5. Docker push script

## Steps

1. Install Terraform if not already
2. Create a copy of the terraform script and update project name, VPC subnet IPs and region
3. Make sure that AWS CLI tools are available
4. Goto the env directory and run `terraform init` to instal dependencies
5. Once done use `terraform plan` to see the resource creation plan
6. If all good, use `terraform apply` to create the infrastructure

## Post Setup

After the setup, the following things need to be done manually,

1. Create a new ECR registry for the docker image
2. Update the docker-push.sh to build and push the image to the ECR
3. Build and push the image
4. Update the docker-pull.sh to pull from the ECR
5. SCP docker-compose.yml, common.env, and docker-pull.sh to the `/project` directory created inside the EC2
6. Update docker-compose.yml and the common.env correctly
7. Use docker-pull.sh to deploy the api server
8. Goto the load balancer and create listeners, configure SSL and other pending stuff.
