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
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import FormView
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


class PostCreate(FormView):
    """
    FormView를 상속받아 구현

    attributes
        template_name
        form_class
        success_url

    method
        form_valid(self, form)
            request는 self.request로 접근 가능
            form.cleaned_data는 바로 사용 가능
            redirect는 정의해줄 필요 없음

    **extra
    post메서드에 login_required 데코레이터 적용
    """
    template_name = 'post/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('post:post-list')

    def form_valid(self, form):
        post = Post.objects.create(author=self.request.user)
        content = form.cleaned_data.get('content', '').strip()
        if content != '':
            PostComment.objects.create(post=post, author=self.request.user, content=content)
        for file in self.request.FILES.getlist('photos'):
            PostPhoto.objects.create(post=post, photo=file)
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post:post-list')
