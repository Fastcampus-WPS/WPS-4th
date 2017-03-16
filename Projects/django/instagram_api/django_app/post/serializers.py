from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'author',
        )
        read_only_fields = (
            'created_date',
        )
