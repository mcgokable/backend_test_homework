from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('user', 'user'),
        ('moderator', 'moderator'),
    )
    role = models.CharField(
        choices=ROLE_CHOICES, default=ROLE_CHOICES[1][0], max_length=500
    )
    bio = models.CharField(max_length=500, blank=True, null=True)
    confirmation_code = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True
    )
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
