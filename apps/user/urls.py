from django.urls import path

from user.views import user_profile, weibo_login, weibo_get_code, logout

urlpatterns = [
    path('profile/', user_profile),
    path('oauth/weibo/login/', weibo_login),
    path('wb/', weibo_get_code),
    path('logout/', logout)
]