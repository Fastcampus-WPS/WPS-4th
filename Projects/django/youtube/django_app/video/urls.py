from django.conf.urls import url

from . import views

app_name = 'video'
urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^bookmark/$', views.bookmark_list, name='bookmark_list'),
    url(r'^bookmark/toggle/$', views.bookmark_toggle, name='bookmark_toggle'),
]
