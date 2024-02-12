# Generated by Django 5.0.1 on 2024-02-01 03:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20210701_1809'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('medication', models.CharField(max_length=255)),
                ('dosage', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('prescribed_at', models.DateTimeField(auto_now_add=True)),
                ('prescribed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescribed_prescriptions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
