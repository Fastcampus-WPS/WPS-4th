from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class CeleryTest(models.Model):
    request_at = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now())
