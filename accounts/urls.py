from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from accounts.views import *

router = routers.DefaultRouter()
router.register('admins', AdminViewSet)
urlpatterns = [
    path('add-admin/', AddAdminView.as_view(), name='add_admin'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('whoami/', GetAdminView.as_view(), name='get_user'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]
