from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q

from apps.users.permissions import AnonWriteOnly, NotAllowed
from apps.users.serializers import AuthRegisterSerializer, UserSerializer, PasswordChangeSerializer, \
    ProfileUpdateSerializer, UserRequestResetPasswordSerializer, UserResetPasswordSerializer
from apps.users.models import User, Roles
from apps.users.services import request_password_reset
from project import settings

from .serializers import DoctorSerializer, PatientSerializer, PharmacyUserSerializer
from .models import Doctor, Patient, PharmacyUser

from rest_framework.decorators import api_view

from .permissions import IsPatient, IsDoctor, IsPharmacyUser
from .services import book_consultation, request_forms, join_consultation, collect_medicine, request_vaccinations, assess_forms, dispense_prescription, dispense_orders


class AuthViewSet(ViewSet):
    def get_permissions(self):
        if (self.action == 'register' and settings.SELF_REGISTER) or self.action == 'request_password_reset':
            permission_classes = [AnonWriteOnly]
        elif self.action == 'change_password':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [NotAllowed]
        return [permission() for permission in permission_classes]

    @action(methods=['post'], detail=False)
    def register(self, request):
        serializer = AuthRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            
            # Handle role-specific data creation 
            if request.data.get('role') == Roles.DOCTOR:
                doctor_data = {'user': user.id, 'specialty': request.data.get('specialty')}
                doctor_serializer = DoctorSerializer(data=doctor_data)
                if doctor_serializer.is_valid(raise_exception=True):
                    doctor_serializer.save()

            if request.data.get('role') == Roles.PATIENT:
                patient_data = {'user': user.id, 'age': request.data.get('age'), 'address': request.data.get('address')}
                patient_serializer = PatientSerializer(data=patient_data)
                if patient_serializer.is_valid(raise_exception=True):
                    patient_serializer.save()

            if request.data.get('role') == Roles.PHARMACY_USER:
                pharmacy_user_data = {'user': user.id, 'registration_number': request.data.get('registration_number')}
                pharmacy_user_serializer = PharmacyUserSerializer(data=pharmacy_user_data)
                if pharmacy_user_serializer.is_valid(raise_exception=True):
                    pharmacy_user_serializer.save() 

            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)         

    @api_view(['POST'])
    def create_doctor(request):
           if request.method == 'POST':
              doctor_serializer = DoctorSerializer(data=request.data)
              if doctor_serializer.is_valid():
                doctor_serializer.save()
                return Response(doctor_serializer.data, status=status.HTTP_201_CREATED)
              return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    @api_view(['POST'])
    def create_patient(request):
           if request.method == 'POST':
              patient_serializer = PatientSerializer(data=request.data)
              if patient_serializer.is_valid():
                patient_serializer.save()
                return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
              return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)            

    @api_view(['POST'])
    def create_pharmacy_user(request):
           if request.method == 'POST':
              pharmacy_user_serializer = PharmacyUserSerializer(data=request.data)
              if pharmacy_user_serializer.is_valid():
                pharmacy_user_serializer.save()
                return Response(pharmacy_user_serializer.data, status=status.HTTP_201_CREATED)
              return Response(pharmacy_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)                                     
                                   

    @action(methods=['post'], detail=False, url_path='change-password')
    def change_password(self, request):
        serializer = PasswordChangeSerializer(data=request.data, instance=request.user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response()

    @action(methods=['post'], detail=False, url_path='request-password-reset')
    def request_password_reset(self, request):
        serializer = UserRequestResetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = get_object_or_404(User, email=request.data['email'])
                request_password_reset(user)
            except Http404:
                pass
            finally:
                message = 'Password reset link has been sent to the registered email address.'
            return Response(message, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='reset-password')
    def reset_password(self, request):
        serializer = UserResetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.user
            user.set_password(serializer.validated_data.get('new_password'))
            user.save()
            return Response()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'me':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def filter_queryset(self, queryset):
        return queryset.filter(Q(is_active=True) & ~Q(role=Roles.SUPER_ADMIN))

    @action(detail=False, methods=['get', 'put', 'patch'])
    def me(self, request):
        if request.method == 'get':
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        else:
            serializer = ProfileUpdateSerializer(data=request.data, instance=request.user, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)

class PatientActionsViewSet(ViewSet):
    permission_classes = [IsPatient]

    @action(methods=['post'], detail=False)
    def book_consultation(self, request):
        # booking a consultation
        consultation_id = book_consultation(request.user, request.data.get('doctor_id'), request.data.get('time_slot'))
        return Response({"consultation_id": consultation_id}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False)
    def request_forms(self, request):
        # requesting forms
        form_type = request.data.get('form_type')
        forms = request_forms(request.user, form_type)
        return Response({"forms": forms}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def join_consultation(self, request):
        # joining a consultation
        consultation_id = request.data.get('consultation_id')
        join_consultation(request.user, consultation_id)
        return Response({"message": "Joined consultation successfully."}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def collect_medicine(self, request):
        # collecting medicine
        prescription_id = request.data.get('prescription_id')
        collect_medicine(request.user, prescription_id)
        return Response({"message": "Medicine collected successfully."}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def request_vaccinations(self, request):
        # requesting vaccinations
        destination_country = request.data.get('destination_country')
        vaccinations = request_vaccinations(request.user, destination_country)
        return Response({"vaccinations": vaccinations}, status=status.HTTP_200_OK)


class DoctorActionsViewSet(ViewSet):
    permission_classes = [IsDoctor]

    @action(methods=['post'], detail=False)
    def assess_forms(self, request):
        # assessing forms
        form_data = request.data.get('form_data')
        assessment_id = assess_forms(request.user, form_data)
        return Response({"assessment_id": assessment_id}, status=status.HTTP_201_CREATED)


class PharmacyUserActionsViewSet(ViewSet):
    permission_classes = [IsPharmacyUser]

    @action(methods=['post'], detail=False)
    def dispense_prescription(self, request):
        # dispensing prescription
        prescription_id = request.data.get('prescription_id')
        dispense_prescription(request.user, prescription_id)
        return Response({"message": "Prescription dispensed successfully."}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def dispense_orders(self, request):
        # dispensing orders
        order_id = request.data.get('order_id')
        dispense_orders(request.user, order_id)
        return Response({"message": "Order dispensed successfully."}, status=status.HTTP_200_OK)