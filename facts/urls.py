from django.urls import path, include

from facts.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', FactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate-fact/', GenerateFact.as_view(), name='generate_fact'),
]
