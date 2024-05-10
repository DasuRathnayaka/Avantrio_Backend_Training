from rest_framework import status
from rest_framework.exceptions import APIException


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Request data does not make sense'
    default_code = 'bad_request'


class ServiceUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class AppointmentUnavailableError(Exception):
    """Exception raised when the appointment booking is not possible due to doctor unavailability."""

    def __init__(self, message="Doctor is not available at this time slot."):
        self.message = message
        super().__init__(self.message)


class ConsultationNotFoundError(Exception):
    """Exception raised when the specified consultation is not found or has ended."""

    def __init__(self, message="Consultation not found or has ended."):
        self.message = message
        super().__init__(self.message)


class MedicineUnavailableError(Exception):
    """Exception raised when the prescribed medicine is unavailable or the prescription is not valid."""

    def __init__(self, message="Prescription is not valid or medicine is unavailable."):
        self.message = message
        super().__init__(self.message)