from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^post-create/$', views.post_create, name='create'),
]
