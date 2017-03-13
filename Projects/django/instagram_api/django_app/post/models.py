from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class PostPhoto(models.Model):
    post = models.ForeignKey(Post)
    photo = models.ImageField(upload_to='post')
