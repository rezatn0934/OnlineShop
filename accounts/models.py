from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import EmailValidator
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50, verbose_name=_("Username"), unique=True)
    email = models.CharField(max_length=50,validators=(EmailValidator, ), verbose_name=_("Email"), unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50, null=True, blank=True)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name=_("Joined Date"), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username


class Customer(models.Model):
    MEMBERSHIP_FREE = 'F'
    MEMBERSHIP_VIP = 'V'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_FREE, 'Free'),
        (MEMBERSHIP_VIP, 'Vip'),
    ]

    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_FREE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
