import os
import re

import requests
from django.core.files.base import File
from django.core.files.temp import NamedTemporaryFile

from member.models import MyUser


class FacebookBackend():
    def authenticate(self, facebook_id, extra_fields=None):
        url_profile = 'https://graph.facebook.com/{user_id}/picture'.format(
            user_id=facebook_id,
        )
        params = {
            'type': 'large',
            'width': '500',
            'height': '500',
        }

        # 메모리상에 임시파일 생성
        temp_file = NamedTemporaryFile(delete=False)
        # 프로필 이미지의 URL에 get요청, stream에 True지정
        r = requests.get(url_profile, params, stream=True)
        # 요청하는 URL에서 파일 확장자를 가져옴
        _, file_ext = os.path.splitext(r.url)

        file_ext = re.sub(r'(\.[^?]+).*', r'\1', file_ext)
        # 페이스북 유저 ID.확장자 로 file_name을 지정
        file_name = '{}{}'.format(
            facebook_id,
            file_ext
        )
        # stream으로 연결된 response에서 1024bytes단위로 데이터를 받아 임시파일에 기록
        for chunk in r.iter_content(1024):
            temp_file.write(chunk)

        # facebook_id가 username인 MyUser를 갖고오거나
        # defaults값을 이용해서 생성
        defaults = {
            'first_name': extra_fields.get('first_name', ''),
            'last_name': extra_fields.get('last_name', ''),
            'email': extra_fields.get('email', ''),
        }
        user, user_created = MyUser.objects.get_or_create(
            defaults=defaults,
            username=facebook_id
        )
        # ImageField의 save메서드에 파일명과 Django에서 지원하는 File객체를 전달
        user.img_profile.save(file_name, File(temp_file))
        return user

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(id=user_id)
        except MyUser.DoesNotExist:
            return None
