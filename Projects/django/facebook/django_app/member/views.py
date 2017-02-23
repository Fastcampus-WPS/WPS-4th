from django.conf import settings
from django.shortcuts import render


def login_fbv(request):
    facebook_app_id = settings.config['facebook']['app_id']
    context = {
        'facebook_app_id': facebook_app_id,
    }
    return render(request, 'member/login.html', context)


def login_facebook(request):
    print(request.GET)
