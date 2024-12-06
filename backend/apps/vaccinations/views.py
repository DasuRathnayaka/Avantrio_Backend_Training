from django.shortcuts import render

from rest_framework import viewsets
from .models import Vaccine, Country, Pharmacy
from .serializers import VaccineSerializer, CountrySerializer, PharmacySerializer
from apps.users.permissions import IsPatient, IsPharmacyUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsPharmacyUser() | IsPatient()]
        return [IsAuthenticated()]
  

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsPatient | IsAdminUser| IsPharmacyUser ]
        return [permission() for permission in permission_classes]    
    
    