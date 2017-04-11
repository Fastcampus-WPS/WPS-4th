from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class CeleryTest(models.Model):
    request_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
