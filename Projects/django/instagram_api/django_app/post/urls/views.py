from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.post_create, name='post-create'),
    url(r'^photo/add/$', views.post_photo_add, name='photo_add'),
]
