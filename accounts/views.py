from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet

# from accounts.permissions import IsAdmin
from accounts.serializers import *


class AdminViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    queryset = Admin.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AdminMiniSerializer
        elif self.action == 'retrieve':
            return AdminSerializer


class AddAdminView(CreateAPIView):
    serializer_class = AddAdminSerializer
    queryset = Admin.objects.all()
