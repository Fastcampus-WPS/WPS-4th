from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    """
    1. 팔로우, 차단을 함께 만들 수 있는 중간자모델을 구현
        검색해보세요!
        django follower twitter model
            class User
                relation
                    through='Relation'

            class Relationship:
                from
                to
                type CharField(choices=(follow, block))

    2. MyUser의
        method:
            follow: 내가 "누군가를" follow하기
            block: 내가 "누군가를" block하기
        property:
            friends: 서로 follow하고 있는 관계
            followers: 나를 follow하고 있는 User들
            following: 내가 follow하고 있는 User들
            block_users: 내가 block한 User들
    """
    relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='relation_user_set',
        through='Relationship',
    )


class Relationship(models.Model):
    TYPE_FOLLOW = 'f'
    TYPE_BLOCK = 'b'

    CHOICES_RELATION_TYPE = (
        (TYPE_FOLLOW, 'Follow'),
        (TYPE_BLOCK, 'Block'),
    )
    from_user = models.ForeignKey(MyUser, related_name='relations_from_user')
    to_user = models.ForeignKey(MyUser, related_name='relations_to_user')
    relation_type = models.CharField(max_length=1, choices=CHOICES_RELATION_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Relation({}) From({}) To({})'.format(
            self.get_relation_type_display(),
            self.from_user.username,
            self.to_user.username,
        )
