from django.urls import path

from user.views import user_profile, weibo_login

urlpatterns = [
    path('profile/', user_profile),
    path('oauth/weibo/login/', weibo_login)
]