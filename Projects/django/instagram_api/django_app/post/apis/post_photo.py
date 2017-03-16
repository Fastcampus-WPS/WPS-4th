from rest_framework import generics

from post.models import PostPhoto
from post.serializers import PostPhotoSerializer

__all__ = (
    'PostPhotoCreate',
    'PostPhotoDestroy',
)


class PostPhotoCreate(generics.CreateAPIView):
    queryset = PostPhoto.objects.all()
    serializer_class = PostPhotoSerializer


class PostPhotoDestroy(generics.DestroyAPIView):
    queryset = PostPhoto.objects.all()
    serializer_class = PostPhotoSerializer
