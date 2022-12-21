from rest_framework import permissions
from rest_framework.views import Request, View
import ipdb

from users.models import User


class GetUserPermissions(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        if request.user.is_superuser:
            return True
        return False


class CreateMoviePermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser


class CreateReviewPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.is_superuser or request.user.is_critic:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        # if request.user.is_critic:
        #     return True
        return request.user.is_authenticated and request.user.is_superuser
