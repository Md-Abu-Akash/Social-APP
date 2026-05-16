from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    phone_number = models.CharField(
        max_length=20,
        unique=True,
        db_index=True
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        null=True,
        blank=True
    )

    profile_image = models.ImageField(
        upload_to='users/profile/',
        null=True,
        blank=True
    )

    bio = models.TextField(
        null=True,
        blank=True
    )

    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return self.username