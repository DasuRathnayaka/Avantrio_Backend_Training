from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

from apps.common.email_templates import EmailTemplates
from apps.common.services import send_mail

from apps.consultations.models import Appointment, FormAssessment, Prescription,FormAssessment
from apps.orders.models import Order
from apps.vaccinations.models import Vaccine
from apps.common.exceptions import AppointmentUnavailableError, ConsultationNotFoundError, MedicineUnavailableError


def request_password_reset(user):
    token = default_token_generator.make_token(user)
    reset_url = '{}/reset-password?email={}&token={}'.format(settings.APP_URL, user.email, token)
    data = {"reset_url": reset_url}
    send_mail(
        'Password Reset Confirmation',
        user.email,
        EmailTemplates.AUTH_PASSWORD_RESET_REQUEST,
        data
    )

def book_consultation(patient, doctor, time_slot):
    if doctor.is_available(time_slot):
        appointment = Appointment.objects.create(patient=patient, doctor=doctor, time=time_slot)
        return appointment
    else:
        raise AppointmentUnavailableError("Doctor is not available at this time slot.")

def request_forms(patient, form_type):
    form = FormAssessment.objects.get(type=form_type)
    return form

def join_consultation(patient, consultation_id):
    consultation = Appointment.objects.get(id=consultation_id)
    if consultation.is_ongoing:
        return consultation
    else:
        raise ConsultationNotFoundError("Consultation not found or has ended.")

def collect_medicine(patient, prescription_id):
    prescription = Prescription.objects.get(id=prescription_id)
    if prescription.is_valid() and prescription.is_medicine_available():
        prescription.collected_by_patient = True
        prescription.save()
        return prescription
    else:
        raise MedicineUnavailableError("Prescription is not valid or medicine is unavailable.")

def request_vaccinations(patient, country):
    recommended_vaccinations = Vaccine.objects.filter(country=country)
    return recommended_vaccinations

def assess_forms(doctor, patient, form_data):
    assessment = FormAssessment.objects.create(doctor=doctor, patient=patient, data=form_data)
    return assessment

def dispense_prescription(pharmacy_user, prescription_id):
    prescription = Prescription.objects.get(id=prescription_id)
    prescription.dispense(pharmacy_user)
    return prescription

def dispense_orders(pharmacy_user, order_id):
    order = Order.objects.get(id=order_id)
    order.dispense(pharmacy_user)
    return order