from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    youtube_id = models.CharField(unique=True, max_length=100)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
