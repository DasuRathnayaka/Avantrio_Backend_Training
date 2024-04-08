from rest_framework import serializers
from .models import Availability, Appointment, FormAssessment, Question, Answer, Note, Prescription, Medicine, Document

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    #def validate(self, data):
        
        # Validate that the appointment slot does not overlap with existing appointments and that the appointment duration is exactly 15 minutes.
        
        #doctor = data['doctor']
        #start_time = data['start_time']
        #end_time = data['end_time']

        # Check if there are any existing appointments for the same doctor and overlapping time slot
        #overlapping_appointments = Appointment.objects.filter(
            #doctor=doctor,
            #start_time__lt=end_time,
            #end_time__gt=start_time
       # ).exclude(pk=self.instance.pk if self.instance else None)

        #if overlapping_appointments.exists():
            #raise serializers.ValidationError("Appointment slot overlaps with existing appointments.")

        # Check if the appointment duration is exactly 15 minutes
        #appointment_duration = end_time - start_time
        #if appointment_duration.total_seconds() != 15 * 60:
            #raise serializers.ValidationError("Appointment duration must be exactly 15 minutes.")

        #return data    

class FormAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAssessment
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
