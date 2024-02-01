from django.db import models
from apps.users.models import User

class Availability(models.Model):
    availability_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date_of_availability = models.DateTimeField()
    #status = 

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.DateTimeField()
    time_extension = models.DateTimeField()
    referrel_letters = models.BooleanField()
    fit_notes = models.BooleanField()
    is_shared_with_GP = models.BooleanField()
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    SCR_consent = models.BooleanField()    

class FormAssessment(models.Model):
    form_assessment_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='form_assessment_doctor')
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='form_assessment_patient')
    is_accessed = models.BooleanField()
    is_subscribed = models.BooleanField()
    is_subscription_valid = models.BooleanField()
    #assessment_status = 

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_type = models.CharField(max_length = 50)

class Answer(models.Model): 
    answer_id = models.AutoField(primary_key=True)  


