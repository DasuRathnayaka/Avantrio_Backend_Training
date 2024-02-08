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
    form_assessment = models.OneToOneField(FormAssessment, on_delete=models.CASCADE, related_name='order_form_assessment')
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='order_appointment')
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE, related_name='order_prescription')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_orders')
    

class Invoice (models.Model):
    charges_type = models.CharField(max_length=10) 
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_invoice')