"""
vi ~/.zshrc
alias mig="./manage.py makemigrations;./manage.py migrate"
"""
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    modified_date = models.DateField(auto_now=True)
    authors = models.ManyToManyField(Author)
    comments_count = models.IntegerField(default=0)
    pingbacks_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title
