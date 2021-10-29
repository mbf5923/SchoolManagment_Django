from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from User.UserManager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    password = None
    is_superuser = None
    groups = None
    is_active = None
    user_permissions = None
    phone = models.PositiveBigIntegerField(unique=True, db_index=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    is_active_user = models.PositiveSmallIntegerField(default=0, help_text='0=not active 1=active 2=ban 3=deleted')
    api_token = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone


class Roles(models.Model):
    title = models.CharField(max_length=255, null=False)
    code_name = models.CharField(max_length=255, null=False, db_index=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.code_name
