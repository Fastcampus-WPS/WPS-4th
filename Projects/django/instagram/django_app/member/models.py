from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    # 다중상속으로 관리자페이지에 로그인 할 수 있는 모든 속성과 메서드를 갖춤
    CHOICES_GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    # 기본값
    # password
    # last_login
    # is_active
    # username이라는 필드를 만들고 USERNAME_FIELD에 추가한 후 makemigrations시도해보기
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER)
    nickname = models.CharField(max_length=20)
    # 프로필 이미지
    img_profile = models.ImageField(upload_to='user', blank=True)
    # 팔로우 목록을 나타내는 필드 구현
    # 언제 팔로우를 했는지도 나타내도록 함 (중간자모델을 사용해야 함)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='follower_set',
        through='RelationShip',
    )

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    # 메서드 추가
    # MyUser를 팔로우 (자신의 following목록에 추가)
    def follow(self, user):
        self.following_relations.create(
            to_user=user
        )

    def unfollow(self, user):
        self.following_relations.filter(
            to_user=user
        ).delete()

    def get_full_name(self):
        return '{} ({})'.format(
            self.nickname,
            self.username
        )

    def get_short_name(self):
        return self.nickname


class RelationShip(models.Model):
    from_user = models.ForeignKey(MyUser, related_name='following_relations')
    to_user = models.ForeignKey(MyUser, related_name='follower_relations')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('from_user', 'to_user',)
        )

    def __str__(self):
        return 'Relation from({}) to({})'.format(
            self.from_user.username,
            self.to_user.username,
        )
