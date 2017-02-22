from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from member.models import MyUser


class MyUserAdmin(UserAdmin):
    pass


admin.site.register(MyUser, MyUserAdmin)
