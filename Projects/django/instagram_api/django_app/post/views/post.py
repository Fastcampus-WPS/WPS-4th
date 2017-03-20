"""
- Class-based view로
    PostList, PostDetail, PostCreate, PostDelete뷰를 작성
        (내용없음)

- 기존 프로젝트의 설정 가져와서 PostList가 작동하도록 구현
    1. settings.py
        STATIC_DIR
            경로 변수 지정
        STATICFILES_DIRS
            STATIC_DIR을 포함하는 튜플 또는 리스트로 변수 할당

    2. 기존 프로젝트의 static폴더 통째로 복사
    3. .gitignore에 django_app/static/css/ 추가
        (CSS파일은 더 이상 소스코드에 포함되지 않음, SCSS파일만 포함)
    4. 기존 프로젝트의 templates폴더 통째로 복사
        (없다면) TEMPLATE_DIR 경로변수 할당 및
                TEMPLATE설정의 TEMPLATE_DIRS에 해당 변수 추가
    5. PostList CBV에 get메서드 작성 및 내부 쿼리를 return
        (Django CBV문서 보면서 진행)
"""
from django.shortcuts import render
from django.views import View

from post.models import Post

__all__ = (
    'PostList',
    'PostDetail',
    'PostDelete',
)


class PostList(View):
    """
    1. 데이터추가
        Postman으로 Post두개 만들고, 각각의 Post에 PostPhoto를 3개 추가
    2. post_list.html에서 posts변수를 loop하며 각 post의 postphoto_set.all을 loop
        postphoto_set을 내부에서 loop하며 내부 loop아이템의 photo.url을 이용해 이미지를 출력
    """
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'post/post_list.html', context)


class PostDetail(View):
    """
    하나의 Post object를 리턴해서 받는 뷰 구현
    """
    pass


class PostDelete(View):
    pass
