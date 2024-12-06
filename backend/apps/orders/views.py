from django.shortcuts import render

from rest_framework import viewsets
from .models import Order, Invoice
from .serializers import OrderSerializer, InvoiceSerializer
from apps.users.permissions import IsPatient, IsPharmacyUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsPatient| IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [ IsPatient | IsAdminUser| IsPharmacyUser ]
        return [permission() for permission in permission_classes]    
    

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsPharmacyUser | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAdminUser| IsPharmacyUser ]
        return [permission() for permission in permission_classes]    
        
    

    