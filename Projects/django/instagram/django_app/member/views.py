"""
1. def login뷰를 만들고
2. member app을 include를 이용해서 'member' namespace를 지정
    instagram/urls.py와 member/urls.py모두 사용
3. login뷰는 member/login URL과 연결되도록 member/urls.py구현
4. login뷰에서는 member/login.html파일을 렌더함
5. settings.py에 TEMPLATE_DIR변수를 할당하고 (os.path.join(BASE_DIR, 'templates'))
    TEMPLATE설정의 DIRS에 추가
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm


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
                return redirect('/admin')
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
