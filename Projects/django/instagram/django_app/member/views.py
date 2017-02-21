"""
1. def login뷰를 만들고
2. member app을 include를 이용해서 'member' namespace를 지정
    instagram/urls.py와 member/urls.py모두 사용
3. login뷰는 member/login URL과 연결되도록 member/urls.py구현
4. login뷰에서는 member/login.html파일을 렌더함
5. settings.py에 TEMPLATE_DIR변수를 할당하고 (os.path.join(BASE_DIR, 'templates'))
    TEMPLATE설정의 DIRS에 추가
"""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from post.models import Post
from .forms import LoginForm, SignupForm, ChangeProfileImageModelForm, SignupModelForm


def login_fbv(request):
    if request.method == 'POST':
        # LoginForm을 사용
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # 전달되어온 POST데이터에서 'username'과 'password'키의 값들을 사용
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # authenticate의 인자로 POST로 전달받은 username, password를 사용
            user = authenticate(username=username, password=password)

            # 만약 인증이 정상적으로 완료되었다면
            # (해당하는 username, password에 일치하는 User객체가 존재할경우)
            if user is not None:
                # Django의 인증관리 시스템을 이용하여 세션을 관리해주기 위해 login()함수 사용
                login(request, user)
                return redirect('post:list')
            # 인증에 실패하였다면 (username, password에 일치하는 User객체가 존재하지 않을 경우)
            else:
                form.add_error(None, 'ID or PW incorrect')

    # GET method로 요청이 왔을 경우
    else:
        # 빈 LoginForm객체를 생성
        form = LoginForm()

    context = {
        'form': form,
    }
    # member/login.html 템플릿을 render한 결과를 리턴
    return render(request, 'member/login.html', context)


def signup_fbv(request):
    """
    회원가입을 구현하세요
    1. member/signup.html파일 생성
    2. SignupForm 클래스 구현
    3. 해당 Form을 사용해서 signup.html템플릿 구성
    4. POST요청을 받아 MyUser객체를 생성 후 로그인
    5. 로그인 완료되면 post_list 뷰로 이동
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.create_user()
            login(request, user)
            return redirect('post:list')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


def signup_model_form_fbv(request):
    if request.method == 'POST':
        form = SignupModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post:list')
    else:
        form = SignupModelForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


@login_required
def profile(request):
    """
    자신의 게시물 수, 자신의 팔로워 수, 자신의 팔로우 수를
    context로 전달, 출력
    """
    post_count = Post.objects.filter(author=request.user).count()
    follower_count = request.user.follower_set.count()
    following_count = request.user.following.count()
    context = {
        'post_count': post_count,
        'follower_count': follower_count,
        'following_count': following_count,
    }
    return render(request, 'member/profile.html', context)


@login_required
def change_profile_image(request):
    """
    해당 유저의 프로필 이미지를 바꾼다
    0. 유저 모델에 img_profile 필드 추가, migrations
    1. change_profile_image.html 파일 작성
    2. ProfileImageForm 생성
    3. 해당 Form을 템플릿에 렌더링
    4. request.method == 'POST'일 때, request.FILES의 값을 이용해서
        request.user의 img_profile을 변경, 저장
    5. 처리 완료 후 member:profile로 이동
    6. profile.html에서 user의 프로필 이미지를 img태그를 사용해서 보여줌
        {{ MEDIA_URL }}을 사용
    """
    if request.method == 'POST':
        # instance에 request.user를 넣어 기존 인스턴스의 필드를 수정하도록 함
        form = ChangeProfileImageModelForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect('member:profile')
    else:
        # instance에 request.user를 넣어 템플릿의 form에서 기존 인스턴스 필드의 정보를 나타내줌
        form = ChangeProfileImageModelForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'member/change_profile_image.html', context)


def logout_fbv(request):
    logout(request)
    return redirect('member:login')
