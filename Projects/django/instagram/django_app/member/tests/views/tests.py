from django.test import TestCase
from django.urls import resolve

from member import views
from member.models import MyUser


def make_user_and_login(client):
    test_username = 'test_user'
    test_password = 'test_password'
    user = MyUser.objects.create_user(test_username, test_password)
    client.post(
        '/member/login/',
        {
            'username': test_username,
            'password': test_password,
        }
    )
    return user


class ProfileViewTest(TestCase):
    def test_user_not_authenticated(self):
        url_profile = '/member/profile/'
        response = self.client.get(url_profile)
        self.assertRedirects(
            response,
            '/member/login/?next={}'.format(
                url_profile
            )
        )


class ChangeProfileImageViewTest(TestCase):
    def test_user_not_authenticated(self):
        url_change_profile_image = '/member/profile/change-profile-image/'
        response = self.client.get(url_change_profile_image)
        self.assertRedirects(
            response,
            '/member/login/?next={}'.format(
                url_change_profile_image
            )
        )

    def test_uses_change_profile_image_template(self):
        make_user_and_login(self.client)
        response = self.client.get('/member/profile/change-profile-image/')
        self.assertTemplateUsed(response, 'member/change_profile_image.html')

    def test_url_resolves_to_change_profile_image_view(self):
        make_user_and_login(self.client)
        found = resolve('/member/profile/change-profile-image/')
        self.assertEqual(found.func, views.change_profile_image)
