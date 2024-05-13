from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Availability, Appointment, FormAssessment, Question, Answer, Note, Prescription, Medicine, Document
from apps.consultations.serializers import AvailabilitySerializer, AppointmentSerializer, FormAssessmentSerializer, QuestionSerializer, AnswerSerializer, NoteSerializer, PrescriptionSerializer, MedicineSerializer, DocumentSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.users.permissions import IsDoctor, IsPatient, IsPharmacyUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsDoctor | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser]
        return [permission() for permission in permission_classes]    
    
    # Nested endpoint for appointments under availability
    @action(detail=True, methods=['get'])
    def appointments(self, request, pk=None):
        availability = self.get_object()
        appointments = availability.appointments.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsDoctor | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser]
        return [permission() for permission in permission_classes]    
    
     # Nested endpoint for prescriptions under appointment
    @action(detail=True, methods=['get'])
    def prescriptions(self, request, pk=None):
        appointment = self.get_object()
        prescriptions = appointment.prescriptions.all()
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)


class FormAssessmentViewSet(viewsets.ModelViewSet):
    queryset = FormAssessment.objects.all()
    serializer_class = FormAssessmentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsPatient | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser]
        return [permission() for permission in permission_classes]    
    
    # Nested endpoint for questions under form assessment
    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        form_assessment = self.get_object()
        questions = form_assessment.questions.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser]
        return [permission() for permission in permission_classes]    

    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsPatient | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser]
        return [permission() for permission in permission_classes]       

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsPatient | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser]
        return [permission() for permission in permission_classes]    
    
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsDoctor | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser]
        return [permission() for permission in permission_classes]    


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsPharmacyUser | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser| IsPharmacyUser ]
        return [permission() for permission in permission_classes]    
    

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [IsPatient | IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsDoctor | IsPatient | IsAdminUser ]
        return [permission() for permission in permission_classes]    
    




