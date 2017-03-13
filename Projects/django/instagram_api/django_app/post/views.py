from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from post.models import Post, PostPhoto

User = get_user_model()


@csrf_exempt
def post_create(request):
    """
    request.POST로 전달된 author_id를 받아 새 post를 생성
    이후 생성된 post의 id값을 HttpResponse로 반환

    받은 author_id에 해당하는 MyUser객체를 가져옴
        실패시 예외처리로 주어진 author_id에 해당하는 User는 없음을 리턴

    urls.py에 연결
        post/urls.py 생성 후
        config/urls.py에는 include로 연결
    """
    if request.method == 'POST':
        try:
            author_id = request.POST['author_id']
            author = User.objects.get(id=author_id)
        except KeyError:
            return HttpResponse('key "author_id" is required field')
        except User.DoesNotExist:
            return HttpResponse('author_id {} is not exist'.format(
                request.POST['author_id']
            ))

        post = Post.objects.create(author=author)
        return HttpResponse('{}'.format(post.pk))
    else:
        return HttpResponse('Post create view')


@csrf_exempt
def post_photo_add(request):
    """
    post_id, photo를 받아서
    PostPhoto객체를 생성
    이후 post_id와 post에 연결된 photo들의 id값을 리턴

    extra:
        post_id, photo가 request.POST, request.DATA에 존재하는지 예외처리
        전달된 post_id에 해당하는 Post객체가 있는지 예외처리
    """
    if request.method == 'POST':
        try:
            post_id = request.POST['post_id']
            photo = request.FILES['photo']
            post = Post.objects.get(id=post_id)
        except KeyError:
            return HttpResponse('post_id and photo is required fields')
        except Post.DoesNotExist:
            return HttpResponse('post_id {} is not exist'.format(
                request.POST['post_id']
            ))
        PostPhoto.objects.create(
            post=post,
            photo=photo
        )
        return HttpResponse('Post: {}, PhotoList: {}'.format(
            post.id,
            [photo.id for photo in post.postphoto_set.all()]
        ))
    else:
        return HttpResponse('Post photo add view')
