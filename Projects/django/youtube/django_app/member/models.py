from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    bookmark_videos = models.ManyToManyField(
        'video.Video',
        blank=True,
    )
