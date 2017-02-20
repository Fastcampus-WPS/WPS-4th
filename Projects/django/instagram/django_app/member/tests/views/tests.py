from django.test import TestCase


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
