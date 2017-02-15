"""
Post List를 보여주는 화면을 구성
1. View에 post_list함수 작성
2. Template에 post_list.html파일 작성
3. View에서 post_list.html을 render한 결과를 리턴하도록 함
4. instagram/urls.py에
    post/urls.py를 연결시킴 (app_name은 post)
5. '/post/'로 접속했을 때 post_list View에 연결되도록
    post/urls.py에 내용을 작성
6. 전체 Post를 가져오는 쿼리셋을
    context로 넘기도록 post_list 뷰에 구현
7. post_list.html에서 {% for %}태그를 사용해
    post_list의 내용을 순회하며 표현

Post Detail (하나의 Post에 대한 상세화면)
1. View에 post_detail함수 작성
2~4. 위와 같음
5. '/post/<숫자>/'로 접속했을 때 post_detail View에
    연결되도록 post/urls.py에 내용 작성
    이 때, post_id라는 패턴명을 가지도록 정규표현식 작성
6. url인자로 전달받은 post_id에 해당하는 Post객체를
    context에 넘겨 post_detail화면을 구성

Post Detail에 댓글작성기능 추가
1. request.method에 따라 로직 분리되도록 if/else블록 추가
2. request.method가 POST일 경우, request.POST에서 'content'키의 값을 가져옴
3. 현재 로그인한 유저는 request.user로 가져오며, Post의 id값은 post_id인자로 전달되므로 두 내용을 사용
4. 위 내용들과 content를 사용해서 Comment객체 생성 및 저장
5. 다시 아까 페이지 (Post Detail)로 redirect해줌
"""
from django.shortcuts import render, redirect

from post.models import Post, Comment


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_id):
    # 인자로 전달된 post_id와 일치하는 id를 가진 Post객체 하나만 조회
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def comment_add(request, post_id):
    if request.method == 'POST':
        # 전달받은 POST데이터에서 'content'값을 할당
        content = request.POST['content']
        # HttpRequest에는 항상 User정보가 전달된다
        user = request.user
        # URL인자로 전달된 post_id값을 사용
        post = Post.objects.get(id=post_id)

        # post의 메서드를 사용해서 Comment객체 생성
        # post.add_comment(user, content)

        # Comment객체를 만들어준다
        Comment.objects.create(
            author=user,
            post=post,
            content=content
        )
        # 다시 해당하는 post_detail로 리다이렉트
        return redirect('post:detail', post_id=post_id)
