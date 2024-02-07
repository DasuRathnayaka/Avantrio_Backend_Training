# Generated by Django 3.2.5 on 2024-02-06 03:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20240205_1223'),
        ('files', '0007_auto_20240205_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='document',
            name='patient',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_documents', to='users.patient'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
