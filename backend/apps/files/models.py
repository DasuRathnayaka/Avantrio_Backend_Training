from pathlib import Path
from time import strftime, localtime

from django.db import models
from django.contrib.auth.models import User
from apps.consultations.models import Appointment
from apps.users.models import Patient
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
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, default=None)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,  related_name='uploaded_documents')
    file = models.ForeignKey(File, on_delete=models.CASCADE, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)

   
  