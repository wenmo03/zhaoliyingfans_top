from django.urls import path
from fans_user.views import FansTopLogin, FansTopRegister, ActiveCode, UsernameOnly, WeiBoLogin

app_name = 'fans_user'

urlpatterns = [
    path('sign_in/', FansTopLogin.as_view(), name='sign_in'),
    path('sign_up/', FansTopRegister.as_view(), name='sign_up'),
    path('active/', ActiveCode.as_view(), name='active'),
    path('usernameOnly/', UsernameOnly.as_view(), name='usernameOnly'),
    path('weibo_login/', WeiBoLogin.as_view(), name='weibo_login'),
]
