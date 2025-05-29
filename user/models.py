from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [
        ('director', _('Director')),
        ('admin', _('Administrator')),
        ('accountant', _('Accountant')),
        ('doctor', _('Doctor')),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="doctor")

    def __str__(self):
        return f"{self.username} ({self.role})"



