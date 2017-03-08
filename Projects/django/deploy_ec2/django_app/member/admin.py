from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from member.models import MyUser


class MyUserAdmin(UserAdmin):
    """
    Django Admin에서 각 User의 Img profile란을 채웠을 때
    media폴더로 업로드되고 해당 링크를 눌렀을 때 정상적으로 표시되도록 처리
        1. MEDIA_ROOT, MEDIA_URL설정
        2. urls.py에 DEBUG일 때 MEDIA_URL이 동작하도록 구현
    """
    fieldsets = (
        (None, {'fields': ('username', 'password', 'img_profile')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(MyUser, MyUserAdmin)
