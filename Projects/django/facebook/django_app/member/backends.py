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

        temp_file = NamedTemporaryFile(delete=False)
        r = requests.get(url_profile, params, stream=True)
        _, file_ext = os.path.splitext(r.url)
        file_ext = re.sub(r'(\.[^?]+).*', r'\1', file_ext)
        file_name = '{}{}'.format(
            facebook_id,
            file_ext
        )
        for chunk in r.iter_content(1024):
            temp_file.write(chunk)

        defaults = {
            'first_name': extra_fields.get('first_name', ''),
            'last_name': extra_fields.get('last_name', ''),
            'email': extra_fields.get('email', ''),
        }
        user, user_created = MyUser.objects.get_or_create(
            defaults=defaults,
            username=facebook_id
        )
        user.img_profile.save(file_name, File(temp_file))
        return user

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(id=user_id)
        except MyUser.DoesNotExist:
            return None
