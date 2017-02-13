"""
1. 모델을 정의
2. 모델이 속한 app을 settings.py의 INSTALLED_APPS에 등록
3. 등록 후 해당 app의 모델을 데이터베이스에 적용시키기위해 makemigrations -> migrate
4. 장고 어드민에 등록시킬 모델을 admin.py에 admin.site.register(모델명)으로 등록
5. 장고 어드민에 로그인 하기위해 ./manage.py createsuperuser로 관리자계정 생성
6. runserver후 localhost:8000/admin으로 접속해서 해당 계정으로 로그인
7. person앱의 Person테이블이 잘 보이는지 확인

- ipython으로 실행하시려면
pip install ipython
# pip install django_extensions
# INSTALLED_APPS에 django_extensions추가
# ./manage.py shell_plus
"""
from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    # 외래키 관계를 자기 자신의 클래스에 대해 갖는다 ('self')
    instructor = models.ForeignKey(
        'self',
        verbose_name='담당 강사',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='student_set',
    )
    owner = models.ForeignKey(
        'self',
        verbose_name='사장님',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='employee_set',
    )
    mentor = models.ForeignKey(
        'self',
        verbose_name='멘토',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='mentee_set',
    )
    name = models.CharField('이름', max_length=60, help_text='성과 이름을 붙여 적으세요')
    shirt_size = models.CharField('셔츠 사이즈', max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    nationality = models.CharField('국적', max_length=100, default='South Korea')

    def __str__(self):
        return self.name


class User(models.Model):
    # 팔로우, 팔로잉을 나타내는 경우
    # MTM필드에 symmetrical=False옵션으로 설정 가능
    following = models.ManyToManyField(
        'self',
        related_name='follower_set',
        symmetrical=False,
    )
    # 단순 친구관계를 나타낼 때는
    # 한 객체가 다른 객체를 '친구'로 선언하면
    # 반대쪽에서도 자동으로 '친구'에 해당됨
    # 이 경우는 기본값 (symmetrical=True)
    #
    # 친구관계에 대한 추가정보가 필요할경우
    # through를 통해서 중간자모델을 참조함
    #
    # 중간자모델을 사용할 경우에는
    # symmetrical이 반드시 False여야 함
    # 이 경우 양쪽이 동시에 친구관계를 맺고자 하면
    # 두 관계를 한 번에 생성해주는 메서드를 생성해 사용해야 함
    #
    # 친구관계에 대한 추가정보 중간자모델이
    # 친구관계를 나태는 User ForeignKey를 두개 초과해서
    # 가질경우, 어떤 User ForeignKey(2개)가 관계를 나타내기위한 필드인지를
    # through_fields로 알려주어야 함
    friends = models.ManyToManyField(
        'self',
        # through='UserFriendsInfo',
        # through_fields=('from_user', 'to_user'),
        # symmetrical=False
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserFriendsInfo(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='+',
    )
    to_user = models.ForeignKey(
        User,
        related_name='+',
    )

    # 중개인이라는 User ForeignKey가 추가로 존재할 경우,
    # 중간자모델을 사용하는곳에서 through_fields를 정의해야함
    recommender = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='recommender_userfriendsinfo_set',
    )
    when = models.DateTimeField(auto_now_add=True)


# 서로 다른 모델간의 MTM에서 중간자모델을 사용하는 경우
class Idol(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(
        Idol,
        # 두 관계를 정의하는 중간자 모델
        through='MemberShip',
        # 이건 기본값이며
        # 만약 중간자모델에서
        # 관계를 형성하는 두 클래스 중
        # 한 클래스라도 한 번을 초과하여 필드로 사용될 경우,
        # through_fields에 내용을 적어줘야한다
        through_fields=('group', 'idol'),
    )

    def __str__(self):
        return self.name


class MemberShip(models.Model):
    group = models.ForeignKey(Group)
    idol = models.ForeignKey(Idol)

    # 추천인이라는 Target모델에 대한 추가 필드가 있을 경우
    # 이 경우에도 through_fields를 정의해줘야함
    date_joined = models.DateTimeField()
    recommender = models.ForeignKey(
        Idol,
        null=True,
        blank=True,
        related_name='recommender_membership_set'
    )

    def __str__(self):
        return '{} - {} ({})'.format(
            self.group.name,
            self.idol.name,
            self.date_joined,
        )


class Article(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Tag(models.Model):
    article = models.ForeignKey(
        Article,
        related_name='tags',
        related_query_name='tag',
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
