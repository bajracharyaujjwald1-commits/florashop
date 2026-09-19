from rest_framework.permissions import BasePermission

class Access_grant(BasePermission):
    message = "No permission"

    """
    Alllows access only to admin users
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
