from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    assessment_type = models.CharField(max_length=50)
    is_prescription_order_accepted = models.BooleanField()
    notification_date = models.DateTimeField(auto_now_add=True)  
    preselected_pharmacy = models.CharField(max_length=10)

class Invoice (models.Model):
    invoice_id = models.AutoField(primary_key=True)
    charges_type = models.CharField(max_length=10) 