from django.shortcuts import render

from rest_framework import viewsets
from .models import Order, Invoice
from .serializers import OrderSerializer, InvoiceSerializer
from apps.users.permissions import IsPatient, IsPharmacyUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsPatient()]
        elif self.action in ['list', 'retrieve']:
            return [IsPharmacyUser() | IsPatient()]
        return [IsAuthenticated()]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsPharmacyUser()]
        elif self.action in ['list', 'retrieve']:
            return [IsPharmacyUser() | IsPatient()]
        return [IsAuthenticated()]
