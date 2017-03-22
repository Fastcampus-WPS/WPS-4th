from django.conf.urls import url
from rest_framework.authtoken import views as authtoken_views
from .. import apis

urlpatterns = [
    url(r'^token-auth/', authtoken_views.obtain_auth_token),
    url(r'^profile/$', apis.ProfileView.as_view()),
]
