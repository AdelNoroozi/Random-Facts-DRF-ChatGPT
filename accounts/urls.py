from django.urls import path, include
from rest_framework import routers
from accounts.models import *
from accounts.views import *

router = routers.DefaultRouter()
router.register('admins', AdminViewSet)
urlpatterns = [
    path('add-admin/', AddAdminView.as_view(), name='add_admin'),
    path('', include(router.urls)),

]
