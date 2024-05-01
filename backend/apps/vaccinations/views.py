from django.shortcuts import render

from rest_framework import viewsets
from .models import Vaccine, Country, Pharmacy
from .serializers import VaccineSerializer, CountrySerializer, PharmacySerializer
from apps.users.permissions import IsPatient, IsPharmacyUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

    

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
