from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Checks if the current user is an Admin or not.
        :param request:
        :param view:
        :return: True if current user is admin, else False
        """
        return request.user.is_admin


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Checks if the request method is one of the Safe methods i.e. Read only.
        :param request:
        :param view:
        :return: True is Safe method else False
        """
        return request.method in SAFE_METHODS
