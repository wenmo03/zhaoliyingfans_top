import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from user.models import FansUser
from zhaoliyingfans_top import settings
from .wb_oauth import OAuthWB
# Create your views here.


def user_profile(request):
    html = '''
    <center><h1>UserProfile</h1></center>
    '''
    return HttpResponse(html)


def weibo_login(request):# 跳转授权页面
    return HttpResponseRedirect(
        'https://api.weibo.com/oauth2/authorize?client_id=' + settings.WEIBO_APP_ID + '&redirect_uri=' + settings.WEIBO_REDIRECT_URI)


def weibo_get_code(request):
    """登录之后，会跳转到这里。需要判断code和state"""
    code = request.GET.get('code', None)
    sina = OAuthWB(settings.WEIBO_APP_ID,
                   settings.WEIBO_APP_KEY,
                   settings.WEIBO_REDIRECT_URI)
    user_info = sina.get_access_token(code)
    time.sleep(0.1)  # 防止还没请求到token就进行下一步
    # 通过uid查询出是否是新用户，新用户则注册登录
    is_user_exist = FansUser.objects.filter(wb_id=user_info['uid']).first()
    if is_user_exist is not None:
        # 存在直接登录
        pass
    else:
        #不存在获取用户信息
        new_user_info = sina.get_user_info(user_info)
        users_dict = {
            "wb_id": new_user_info['id'],
            # 'description': new_user_info['description'],
            "head": new_user_info['profile_image_url'],
            "nickname": new_user_info['name'],
        }
        users_table_obj = FansUser.objects.create(**users_dict).id
        return HttpResponse(users_table_obj)
    data = {
        'code': 200,
    }
    return HttpResponse(data)
