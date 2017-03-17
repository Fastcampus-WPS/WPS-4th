from rest_framework import serializers

from post.models import PostPhoto

__all__ = (
    'PostPhotoSerializer',
)


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = (
            'pk',
            'post',
            'photo',
        )
