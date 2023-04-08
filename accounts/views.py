from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from accounts.serializers import *


class AdminViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    queryset = Admin.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AdminMiniSerializer
        elif self.action == 'retrieve':
            return AdminSerializer
        elif self.action == 'create':
            return AddAdminSerializer
