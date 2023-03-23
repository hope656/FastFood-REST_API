from rest_framework.permissions import BasePermission

class IsAdminOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_staff):
            return True
        return obj == request.user