from django.shortcuts import redirect


def index(request):
    """
    유저가 로그인했을 경우, post:list로 이동
    로그인하지 않았을 경우, member:signup으로 이동

    테스트 작성
        1. index URL로 접근했을 때, 로그인 하지 않았을 경우 member:signup으로 가는지 확인
        2. 위와 같은데 로그인 했을 경우 post:list로 가는지 확인
    """
    if request.user.is_authenticated:
        return redirect('post:list')
    else:
        return redirect('member:signup')
