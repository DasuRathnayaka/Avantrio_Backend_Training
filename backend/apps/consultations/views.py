from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Availability, Appointment, FormAssessment, Question, Answer, Note, Prescription, Medicine, Document
from apps.consultations.serializers import AvailabilitySerializer, AppointmentSerializer, FormAssessmentSerializer, QuestionSerializer, AnswerSerializer, NoteSerializer, PrescriptionSerializer, MedicineSerializer, DocumentSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.users.permissions import IsDoctor, IsPatient, IsPharmacyUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsDoctor()]
        elif self.action in ['list', 'retrieve']:
            return [IsDoctor() | IsPatient()]
        return [IsAuthenticated()]
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsDoctor()]
        elif self.action in ['list', 'retrieve']:
            return [IsDoctor() | IsPatient()]
        return [IsAuthenticated()]


class FormAssessmentViewSet(viewsets.ModelViewSet):
    queryset = FormAssessment.objects.all()
    serializer_class = FormAssessmentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsPatient()]
        elif self.action in ['list', 'retrieve']:
            return [IsDoctor() | IsPatient()]
        return [IsAuthenticated()]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsDoctor() | IsPatient()]
        return [IsAuthenticated()]

    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsPatient()]
        elif self.action in ['list', 'retrieve']:
                return [IsDoctor() | IsPatient()]
        return [IsAuthenticated()]     

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsPatient()]
        elif self.action in ['list', 'retrieve']:
                return [IsDoctor() | IsPatient()]
        return [IsAuthenticated()] 
    
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsDoctor()]
        elif self.action in ['retrieve', 'update']:
            return [IsPharmacyUser() | IsPatient()]
        return [IsAuthenticated()]


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsPharmacyUser()]
        elif self.action in ['list', 'retrieve']:
                return [IsDoctor() | IsPatient() | IsPharmacyUser() ]
        return [IsAuthenticated()]
    

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsPatient()]
        elif self.action in ['list', 'retrieve']:
                return [IsDoctor() | IsPatient()]
        return [IsAuthenticated()] 

