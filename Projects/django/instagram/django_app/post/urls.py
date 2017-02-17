from django.conf.urls import url

from . import views

app_name = 'post'
urlpatterns = [
    url(r'^$',
        views.post_list,
        name='list'),
    url(r'^add/$',
        views.post_add,
        name='add'),
    url(r'^(?P<post_id>[0-9]+)/delete/$',
        views.post_delete,
        name='delete'),
    url(r'^(?P<post_id>[0-9]+)/$',
        views.post_detail,
        name='detail'),
    url(r'^(?P<post_id>[0-9]+)/comment/add/$',
        views.comment_add,
        name='comment_add'),
    url(r'^(?P<post_id>[0-9]+)/like/toggle/$',
        views.post_like_toggle,
        name='like_toggle'),
    url(r'^(?P<post_id>[0-9]+)/comment/(?P<comment_id>[0-9]+)/delete/$',
        views.comment_delete,
        name='comment_delete'),
]
