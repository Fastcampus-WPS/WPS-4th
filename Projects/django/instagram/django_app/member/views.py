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
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm


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


def profile(request):
    """
    1. button 1개 (로그아웃)이 존재하는 member/profile.html을 render해주는 view
    2. 메인의 우측 위 사람모양 아이콘에 이 뷰로 오는 링크를 연결
    """
    context = {

    }
    return render(request, 'member/profile.html', context)


def logout_fbv(request):
    logout(request)
    return redirect('member:login')
