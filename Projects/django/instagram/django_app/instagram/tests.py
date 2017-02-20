from django.test import Client
from django.test import LiveServerTestCase

from member.models import MyUser


class IndexTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_user_is_not_authenticated_redirect_to_signup(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/member/signup/')

    def test_user_is_authentiacted_redirect_to_(self):
        test_username = 'test_user'
        test_password = 'test_password'
        MyUser.objects.create_user(test_username, test_password)
        self.client.post(
            '/member/login/',
            {
                'username': test_username,
                'password': test_password,
            }
        )
        response = self.client.get('/')
        self.assertRedirects(response, '/post/')