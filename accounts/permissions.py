from rest_framework.permissions import BasePermission


class FactViewSetPermissions(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        else:
            return request.user.is_staff


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
