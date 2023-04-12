from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

# from accounts.permissions import IsAdmin
from accounts.permissions import IsSuperUser
from accounts.serializers import *


class AdminViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):
    queryset = Admin.objects.all()
    permission_classes = (IsSuperUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return AdminMiniSerializer
        else:
            return AdminSerializer

    @action(detail=True, methods=['PATCH', ])
    def activate_admin_account(self, request, pk=None):
        admin = Admin.objects.get(id=pk)
        if admin.is_active:
            response = {'message': 'admin account is already active.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            admin.is_active = True
            admin.save()
            response = {'message': 'account activated successfully.'}
            return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['PATCH', ])
    def deactivate_admin_account(self, request, pk=None):
        admin = Admin.objects.get(id=pk)
        if not admin.is_active:
            response = {'message': 'admin account is already deactivated.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            admin.is_active = False
            admin.save()
            response = {'message': 'account deactivated successfully.'}
            return Response(response, status=status.HTTP_200_OK)


class AddAdminView(CreateAPIView):
    serializer_class = AddAdminSerializer
    queryset = Admin.objects.all()
    permission_classes = (IsSuperUser,)


class GetAdminView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            admin = request.user
            serializer = AdminSerializer(admin)
            return Response(serializer.data)
        else:
            raise AuthenticationFailed('not authenticated')


class ChangePasswordView(APIView):
    def patch(self, request):
        if request.user.is_authenticated:
            admin = request.user
            try:
                current_password = request.data['current_password']
                new_password = request.data['new_password']
            except Exception as e:
                response = {'message': f'field error:{str(e)}'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                if admin.check_password(current_password):
                    validate_password(new_password)
                    if current_password == new_password:
                        response = {'message': 'new password can not be the same as current password.'}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        admin.password = make_password(new_password)
                        admin.save()
                        response = {'message': 'password changed successfully.'}
                        return Response(response, status=status.HTTP_202_ACCEPTED)
                else:
                    response = {'message': 'incorrect password.'}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

        else:
            raise AuthenticationFailed('not authenticated')
