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
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def login(request):
    """
    request.method == 'POST'일 때와
    아닐 때의 동작을 구분
    POST일 때는 authenticate, login을 거치는 로직을 실행
    GET일 때는 member/login.html을 render하여 return하도록 함
    """
    if request.method == 'POST':
        # html파일에서 POST요청을 보내기위해서
        # form을 정의하고, input요소 2개의 name을
        # username, password로 설정하고
        # button type submit을 실행

        # 전달되어온 POST데이터에서 'username'과 'password'키의 값들을 사용
        username = request.POST['username']
        password = request.POST['password']
        # authenticate의 인자로 POST로 전달받은 username, password를 사용
        user = authenticate(username=username, password=password)

        # 만약 인증이 정상적으로 완료되었다면
        # (해당하는 username, password에 일치하는 User객체가 존재할경우)
        if user is not None:
            # Django의 인증관리 시스템을 이용하여 세션을 관리해주기 위해 login()함수 사용
            login(request, user)
            return HttpResponse('Login Success')
        # 인증에 실패하였다면 (username, password에 일치하는 User객체가 존재하지 않을 경우)
        else:
            return HttpResponse('Login failed')
    # GET method로 요청이 왔을 경우
    else:
        # member/login.html 템플릿을 render한 결과를 리턴
        return render(request, 'member/login.html')
