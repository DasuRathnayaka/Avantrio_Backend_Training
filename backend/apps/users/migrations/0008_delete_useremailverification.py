# Generated by Django 3.2.5 on 2024-02-07 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_useremailverification_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserEmailVerification',
        ),
    ]