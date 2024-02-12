# Generated by Django 3.2.5 on 2024-02-06 03:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20240205_1223'),
        ('vaccinations', '0001_initial'),
        ('consultations', '0002_auto_20240205_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='form_assessment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='consultations.formassessment'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='availability',
            name='appointment',
            field=models.OneToOneField( on_delete=django.db.models.deletion.CASCADE, to='consultations.appointment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='medicine',
            field=models.ManyToManyField(to='consultations.Medicine'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='pharmacy',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy', to='vaccinations.pharmacy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='form_assessment',
            field=models.ManyToManyField(to='consultations.FormAssessment'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.BigAutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='availability',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formassessment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
