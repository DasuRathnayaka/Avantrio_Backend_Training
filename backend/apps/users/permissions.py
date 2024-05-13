from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UpdateOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'PUT'


class AnonWriteOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'


class HasResourcePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin_user()


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_super_admin()


class NotAllowed(BasePermission):
    def has_permission(self, request, view):
        raise PermissionDenied()

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'DOCTOR'

class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'PATIENT'

class IsPharmacyUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'PHARMACY USER'
    
