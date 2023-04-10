from rest_framework.permissions import BasePermission


class FactViewSetPermissions(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        else:
            return request.user.is_staff
