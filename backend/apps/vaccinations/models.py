from django.db import models
from apps.users.models import PharmacyUser

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=20)
    vaccine_availability = models.BooleanField()

class Country(models.Model):  
    country_code = models.CharField(max_length=10)
    vaccine = models.ManyToManyField(Vaccine, related_name='vaccine_countries')

class Pharmacy(models.Model):
    postal_code = models.CharField(max_length=50)
    vaccine = models.ManyToManyField(Vaccine, related_name='vaccine_pharmacies')
    owner = models.OneToOneField(PharmacyUser, default=None ,on_delete=models.CASCADE, related_name='pharmacy')
