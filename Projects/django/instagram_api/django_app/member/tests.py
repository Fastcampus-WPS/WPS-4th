from django.test import LiveServerTestCase

from member.models import MyUser


class RelationTest(LiveServerTestCase):
    @staticmethod
    def create_dummy_users(num):
        return [MyUser.objects.create(username='user{}'.format(i)) for i in range(num)]
        # users = []
        # for i in range(num):
        #     user = MyUser.objects.create(
        #         username='user{}'.format(i),
        #         password='test_password'
        #     )
        #     users.append(user)
        # return users

    def test_following(self):
        users = self.create_dummy_users(10)
        users[0].follow(users[1])
        users[0].follow(users[2])
        users[0].follow(users[3])
        users[0].follow(users[4])

        self.assertEqual(users[0].following.count(), 4)

    def test_followers(self):
        pass

    def test_block_users(self):
        pass

    def test_friends(self):
        pass
