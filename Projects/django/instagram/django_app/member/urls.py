from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    url(r'^login/$', views.login_fbv, name='login'),
    url(r'^logout/$', views.logout_fbv, name='logout'),
    url(r'^signup/$', views.signup_fbv, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
]