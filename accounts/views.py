from django.shortcuts import render
from rest_framework import mixins
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
                   GenericViewSet):
    queryset = Admin.objects.all()
    permission_classes = (IsSuperUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return AdminMiniSerializer
        elif self.action == 'retrieve':
            return AdminSerializer


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
