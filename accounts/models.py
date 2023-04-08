from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_admin(self, username, password=None, is_active=True):
        if not username:
            raise ValueError('username is required')
        if not password:
            raise ValueError('password is required')
        admin_instance = self.model(
            username=username
        )
        admin_instance.password = make_password(password)
        admin_instance.is_staff = True
        admin_instance.is_superuser = False
        admin_instance.active = is_active
        admin_instance.save(using=self._db)
        return admin_instance

    def create_superuser(self, username, password=None):
        superuser = self.create_admin(
            username=username,
            password=password
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class Admin(AbstractUser):
    modified_at = models.DateTimeField(auto_now=True, null=True)

    objects = UserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Admin')
        verbose_name_plural = _('Admins')
