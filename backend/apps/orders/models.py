from django.db import models
from apps.consultations.models import FormAssessment
from apps.consultations.models import Appointment
from apps.consultations.models import Prescription
from apps.users.models import Patient


class Order(models.Model):
    assessment_type = models.CharField(max_length=50)
    is_prescription_order_accepted = models.BooleanField()
    notification_date = models.DateTimeField(auto_now_add=True)  
    preselected_pharmacy = models.CharField(max_length=10)
    form_assessment = models.OneToOneField(FormAssessment, on_delete=models.CASCADE)
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    

class Invoice (models.Model):
    charges_type = models.CharField(max_length=10) 
    order = models.OneToOneField(Order, on_delete=models.CASCADE)