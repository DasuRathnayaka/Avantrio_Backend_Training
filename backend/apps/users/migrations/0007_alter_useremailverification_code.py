# Generated by Django 3.2.5 on 2024-02-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_useremailverification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremailverification',
            name='code',
            field=models.PositiveIntegerField(max_length=6),
        ),
    ]
