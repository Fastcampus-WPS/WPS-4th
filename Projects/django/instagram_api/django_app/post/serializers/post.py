from rest_framework import serializers

from member.serializers import UserSerializer
from post.models import Post
from post.serializers.post_photo import PostPhotoSerializer

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    """
    목표 1.
        author필드의 값이 pk가 아닌, 하나의 Object(dict)로 나타나도록 수정
        http://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects

    1. 관련 테스트코드 작성
        post_list, post_create부분
    2. 해당 테스트코드가 작동하도록 PostSerializer를 수정 및 UserSerializer작성
    3. 테스트 및 포스트맨 작동 확인

    목표 2.
        Post에 연결된 PostPhoto를 리스트 내부의 Object형태로 리턴
        'author': {<author object>},
        'postphoto_set': [
            {
                'pk': <PostPhoto pk>,
                'photo': <PostPhoto photo field url>,
            },
            {
                'pk': <PostPhoto pk>,
                'photo': <PostPhoto photo field url>,
            },
        ]

        1. 관련 테스트코드 작성
            post_list, post_create부분
        2. 해당 테스트코드가 작동하도록 PostSerializer를 수정 및 PostPhotoSerializer작성
        3. 테스트 및 포스트맨 작동 확인
        4. postphoto_set의 이름을 photo_list로 변경
            http://www.django-rest-framework.org/api-guide/serializers/#specifying-fields-explicitly

    목표 3.
        post-list요청시 Pagination될 수 있도록 변경

    1. 관련 테스트코드 작성 (가능하면)
    2. Pagination문서 보고 CustomPagination구현
    3. pagination_class에 지정
    4. 요청결과를 확인
    """
    author = UserSerializer(read_only=True)
    postphoto_set = PostPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'created_date',
            'postphoto_set',
        )
        read_only_fields = (
            'created_date',
        )
