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

    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    

class FormAssessmentViewSet(viewsets.ModelViewSet):
    queryset = FormAssessment.objects.all()
    serializer_class = FormAssessmentSerializer

    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    
