# Generated by Django 3.2.5 on 2024-02-01 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FormAssessment',
            fields=[
                ('form_assessment_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_accessed', models.BooleanField()),
                ('is_subscribed', models.BooleanField()),
                ('is_subscription_valid', models.BooleanField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_assessment_doctor', to=settings.AUTH_USER_MODEL)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_assessment_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('availability_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('date_of_availability', models.DateTimeField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('time_extension', models.DateTimeField()),
                ('referrel_letters', models.BooleanField()),
                ('fit_notes', models.BooleanField()),
                ('is_shared_with_GP', models.BooleanField()),
                ('extra_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('SCR_consent', models.BooleanField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
