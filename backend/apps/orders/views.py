from django.shortcuts import render

from rest_framework import viewsets
from .models import Order, Invoice
from .serializers import OrderSerializer, InvoiceSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
