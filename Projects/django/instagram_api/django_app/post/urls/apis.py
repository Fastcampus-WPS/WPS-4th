from django.conf.urls import url

from .. import apis as views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
]
