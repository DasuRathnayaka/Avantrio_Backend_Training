from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Availability, Appointment, FormAssessment, Question, Answer, Note, Prescription, Medicine, Document
from apps.consultations.serializers import AvailabilitySerializer, AppointmentSerializer, FormAssessmentSerializer, QuestionSerializer, AnswerSerializer, NoteSerializer, PrescriptionSerializer, MedicineSerializer, DocumentSerializer
from rest_framework.response import Response
from rest_framework import status

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Validate appointment data
        try:
            validated_data = serializer.validated_data
            doctor = validated_data['doctor']
            start_time = validated_data['start_time']
            end_time = validated_data['end_time']
            
            # Check for overlapping appointments
            overlapping_appointments = Appointment.objects.filter(
                doctor=doctor,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            if overlapping_appointments.exists():
                return Response({"error": "Appointment slot overlaps with existing appointments."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if appointment duration is exactly 15 minutes
            appointment_duration = end_time - start_time
            if appointment_duration.total_seconds() != 15 * 60:
                return Response({"error": "Appointment duration must be exactly 15 minutes."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Proceed with creating the appointment if validations pass
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except KeyError:
            return Response({"error": "Invalid appointment data."}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Validate appointment data
        try:
            validated_data = serializer.validated_data
            doctor = validated_data['doctor']
            start_time = validated_data['start_time']
            end_time = validated_data['end_time']
            
            # Check for overlapping appointments
            overlapping_appointments = Appointment.objects.filter(
                doctor=doctor,
                start_time__lt=end_time,
                end_time__gt=start_time
            ).exclude(pk=instance.pk)
            if overlapping_appointments.exists():
                return Response({"error": "Appointment slot overlaps with existing appointments."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if appointment duration is exactly 15 minutes
            appointment_duration = end_time - start_time
            if appointment_duration.total_seconds() != 15 * 60:
                return Response({"error": "Appointment duration must be exactly 15 minutes."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Proceed with updating the appointment if validations pass
            self.perform_update(serializer)
            return Response(serializer.data)
        except KeyError:
            return Response({"error": "Invalid appointment data."}, status=status.HTTP_400_BAD_REQUEST)


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
