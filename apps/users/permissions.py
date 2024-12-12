from rest_framework.permissions import BasePermission

class IsActivated(BasePermission):
    def has_permission(self, request, view):
        if not bool(request.user and request.user.is_authenticated):
            return False
        return request.user.is_activated 