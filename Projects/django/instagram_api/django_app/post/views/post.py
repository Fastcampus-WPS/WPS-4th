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
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView

from post.forms import PostForm
from post.models import Post, PostComment, PostPhoto

__all__ = (
    'PostList',
    'PostDetail',
    'PostCreate',
    'PostDelete',
)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    """
    DetailView를 상속받아서 구현되도록 해보세요
    """
    model = Post


class PostCreate(View):
    """
    PostForm을 사용
        fields
            content
            photos
    POST요청을 받았을 때,
    1. 해당 request.user를 author로 하는 Post 인스턴스 생성
    2. 만약 form.cleaned_data['content']가 빈 값이 아니면 PostComment 인스턴스 생성
    3. request.FILES.getlist('photos')를 loop하며 PostPhoto 인스턴스 생성
    4. return redirect('post:post-list')
    """
    form_class = PostForm
    template_name = 'post/post_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # 1. 해당 request.user를 author로 하는 Post 인스턴스 생성
        post = Post.objects.create(author=request.user)

        # 2. 만약 form.cleaned_data['content']가 빈 값이 아니면 PostComment인스턴스 생성
        #   is_valid()이후
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            content = form.cleaned_data.get('content', '').strip()
            if content != '':
                PostComment.objects.create(
                    post=post,
                    author=request.user,
                    content=content
                )

            # 3. request.FILES.getlist('photos')를 loop하며 PostPhoto 인스턴스 생성
            for file in request.FILES.getlist('photos'):
                PostPhoto.objects.create(
                    post=post,
                    photo=file
                )
            return redirect('post:post-list')
        else:
            return HttpResponse(form.errors)


class PostDelete(View):
    pass
