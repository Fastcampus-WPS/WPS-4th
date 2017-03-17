from rest_framework import serializers

from member.serializers import UserSerializer
from post.models import Post

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    """
    목표
        author필드의 값이 pk가 아닌, 하나의 Object(dict)로 나타나도록 수정
        http://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects

    1. 관련 테스트코드 작성
        post_list, post_create부분
    2. 해당 테스트코드가 작동하도록 PostSerializer를 수정 및 UserSerializer작성
    3. 테스트 및 포스트맨 작동 확인
    """
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'created_date',
        )
        read_only_fields = (
            'created_date',
        )
