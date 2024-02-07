from django.db import models

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=20)
    vaccine_availability = models.BooleanField()

class Country(models.Model):  
    country_code = models.CharField(max_length=10)
    vaccine = models.ManyToManyField(Vaccine)

class Pharmacy(models.Model):
    postal_code = models.CharField(max_length=50)
    vaccine = models.ManyToManyField(Vaccine)
    
