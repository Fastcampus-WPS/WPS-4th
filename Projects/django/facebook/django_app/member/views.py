from pprint import pprint

import requests
from django.shortcuts import render

from facebook import settings


def login_fbv(request):
    facebook_app_id = settings.config['facebook']['app_id']
    context = {
        'facebook_app_id': facebook_app_id,
    }
    return render(request, 'member/login.html', context)


def login_facebook(request):
    APP_ID = settings.config['facebook']['app_id']
    SECRET_CODE = settings.config['facebook']['secret_code']
    REDIRECT_URI = 'http://localhost:8000/member/login/facebook/'
    APP_ACCESS_TOKEN = '{app_id}|{secret_code}'.format(
        app_id=APP_ID,
        secret_code=SECRET_CODE
    )

    # login_fbv에서 페이스북 로그인으로 이동 후,
    # 정상적인 로그인 후 (정상적으로 로그인 시 request.GET에 'code' parameter가 추가됨)
    # redirect_uri를 이용해 다시 login_facebook으로 돌아온 후의 동작
    if request.GET.get('code'):
        code = request.GET.get('code')

        # 전달받은 code값을 이용해서 access_token을 요청함
        url_request_access_token = 'https://graph.facebook.com/v2.8/oauth/access_token'
        params = {
            'client_id': APP_ID,
            'redirect_uri': REDIRECT_URI,
            'client_secret': SECRET_CODE,
            'code': code,
        }
        r = requests.get(url_request_access_token, params=params)
        dict_access_token = r.json()
        USER_ACCESS_TOKEN = dict_access_token['access_token']
        print('ACCESS_TOKEN : %s' % USER_ACCESS_TOKEN)

        # 유저 액세스 토큰과 앱 엑세스 토큰을 사용해서 토큰 검증을 거친다
        url_debug_token = 'https://graph.facebook.com/debug_token'
        params = {
            'input_token': USER_ACCESS_TOKEN,
            'access_token': APP_ACCESS_TOKEN,
        }
        r = requests.get(url_debug_token, params=params)
        dict_debug_token = r.json()
        pprint(dict_debug_token)
        USER_ID = dict_debug_token['data']['user_id']
        print('USER_ID : %s' % USER_ID)
