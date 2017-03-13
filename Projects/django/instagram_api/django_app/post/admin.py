from django.contrib import admin

from post.models import Post
from post.models import PostPhoto

admin.site.register(Post)
admin.site.register(PostPhoto)
