from django.db import models

class Vaccine(models.Model):
    vaccine_id = models.AutoField(primary_key=True)
    vaccine_name = models.CharField(max_length=20)
    vaccine_availability = models.BooleanField()

class Country(models.Model):  
    country_id = models.AutoField(primary_key=True) 
    country_code = models.CharField(max_length=10)

class Pharmacy(models.Model):
    pharmacy_id = models.AutoField(primary_key=True)
    postal_code = models.CharField(max_length=50)
