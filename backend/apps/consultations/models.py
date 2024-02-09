from django.db import models
from apps.users.models import Doctor
from apps.users.models import Patient
from apps.vaccinations.models import Pharmacy
from django.conf import settings
from apps.files.models import File

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name = 'availabilities')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date_of_availability = models.DateTimeField()
    appointment = models.OneToOneField('Appointment',on_delete=models.CASCADE, related_name='availability')

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    time = models.DateTimeField()
    time_extension = models.DateTimeField()
    referrel_letters = models.BooleanField()
    fit_notes = models.BooleanField()
    is_shared_with_GP = models.BooleanField()
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    SCR_consent = models.BooleanField()    

class FormAssessment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='form_assessments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='form_assessments')
    is_accessed = models.BooleanField()
    is_subscribed = models.BooleanField()
    is_subscription_valid = models.BooleanField()

class Question(models.Model):
    question_type = models.CharField(max_length = 50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='questions')
    form_assessment = models.ManyToManyField(FormAssessment,related_name='questions')

class Answer(models.Model): 
    answered_date =  models.DateTimeField(default = None) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='answers')
    form_assessment = models.ForeignKey(FormAssessment, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', default = None)

class Note(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, default=None, related_name='notes')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)   

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, default=None, related_name='prescription')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='prescriptions')
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()   
    prescribed_at = models.DateTimeField(auto_now_add=True) 
    medicine = models.ManyToManyField('Medicine', related_name='prescriptions')
    form_assessment = models.OneToOneField(FormAssessment,on_delete=models.CASCADE, default=None, related_name='prescription' )

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    is_available =  models.BooleanField()
    
class Document(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE,related_name='appointment_documents',default=None)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,  related_name='uploaded_documents')
    file = models.ForeignKey(File, on_delete=models.CASCADE, default=None, related_name='document')
    uploaded_at = models.DateTimeField(auto_now_add=True)
