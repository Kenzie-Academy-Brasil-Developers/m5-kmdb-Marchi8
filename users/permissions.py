from rest_framework import permissions
from rest_framework.views import Request, View


class GetUserPermissions(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        if request.user.is_superuser:
            return True
        return False
