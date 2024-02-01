from pathlib import Path
from time import strftime, localtime

from django.db import models
from django.contrib.auth.models import User
from apps.consultations.models import Appointment
from django.conf import settings

import uuid


def file_path(instance, filename):
    return '{0}/{1}{2}'.format(strftime('%Y/%m/%d', localtime()), uuid.uuid4(), Path(filename).suffix)


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=False, null=False, upload_to=file_path)
    file_name = models.TextField()

    def __str__(self):
        return self.file_name

class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, default=None)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='uploaded_documents')
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, default=None)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)   

class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, default=None)
    prescribed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='prescribed_prescriptions')
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()
    prescribed_at = models.DateTimeField(auto_now_add=True)    
  