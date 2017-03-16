from rest_framework import generics

from post.models import PostPhoto

__all__ = (
    'PostPhotoCreate',
    'PostPhotoDestroy',
)


class PostPhotoCreate(generics.CreateAPIView):
    queryset = PostPhoto.objects.all()


class PostPhotoDestroy(generics.DestroyAPIView):
    queryset = PostPhoto.objects.all()
