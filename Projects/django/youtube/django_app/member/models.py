from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    bookmark_videos = models.ManyToManyField(
        'video.Video',
        blank=True,
        # created_date를 기록하기 위한 중간자모델 정의
        through='BookmarkVideo',
        # Video인스턴스가 자신을 Bookmark한 MyUser를 참조하고 싶을 때 사용하는 이름
        related_name='bookmark_user_set'
    )


class BookmarkVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    video = models.ForeignKey('video.Video')
    created_date = models.DateTimeField(auto_now_add=True)
