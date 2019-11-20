import time
import uuid

import requests
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import FansUser
from user.serializers import RegisterFansUserSerializer
from zhaoliyingfans_top import settings
from .wb_oauth import OAuthWB


# Create your views here.


def user_profile(request):
    html = '''
    <center><h1>UserProfile</h1></center>
    '''
    return HttpResponse(html)


def weibo_login(request):  # 跳转授权页面
    return HttpResponseRedirect(
        'https://api.weibo.com/oauth2/authorize?client_id=' + settings.WEIBO_APP_ID + '&redirect_uri=' + settings.WEIBO_REDIRECT_URI)


def weibo_get_code(request):
    """登录之后，会跳转到这里。需要判断code和state"""
    code = request.GET.get('code', None)
    sina = OAuthWB(settings.WEIBO_APP_ID,
                   settings.WEIBO_APP_KEY,
                   settings.WEIBO_REDIRECT_URI)
    user_info = sina.get_access_token(code)
    print(user_info)
    time.sleep(0.1)  # 防止还没请求到token就进行下一步
    # 通过uid查询出是否是新用户，新用户则注册登录
    is_user_exist = FansUser.objects.filter(wb_id=user_info['uid']).first()
    print('==============', is_user_exist, '====================')
    if is_user_exist is not None:
        # 存在直接登录
        pass
    else:
        # 不存在获取用户信息
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


def logout(request):
    url = 'https://api.weibo.com/oauth2/revokeoauth2'
    the_access_token = '2.00j9j__GSwSE5Bb85f4667040qALuW'
    querystring = {
        "access_token": the_access_token
    }
    response = requests.request("GET", url, params=querystring)
    return HttpResponse(response)


class user_register(APIView):
    def post(self, request):
        reg_result = self.do_register(request)
        if reg_result[0]:
            return Response(reg_result[1])

        fans_user_serializers = RegisterFansUserSerializer(data=request.data)
        if fans_user_serializers.is_valid():
            fans_user_serializers.save()

        # 激活注册用户，token有效期一小时
        token = self.make_token()
        username = request.data.get('username')
        cache.set(token, username, 60 * 60)

        data = {
            'msg': 'success',
            'data': fans_user_serializers.validated_data,
            'token': token,
        }
        return Response(data)

    def do_register(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        repassword = request.data.get('repassword')
        email = request.data.get('email')

        if username == '':
            msg = {
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '用户名不能为空',
            }
            return True, msg

        if password == '':
            msg = {
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '密码不能为空',
            }
            return True, msg

        if repassword == '':
            msg = {
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '第二次输入密码不能为空',
            }
            return True, msg

        if email == '':
            msg = {
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '邮箱不能为空',
            }
            return True, msg

        if password != repassword:
            msg = {
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '两次输入密码不一致',
            }
            return True, msg
        user = self.username_exist(request.data.get('username'))
        if user:
            msg = {
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '用户名已存在',
            }
            return True, msg
        msg = {
            'status': status.HTTP_200_OK,
            'msg': '注册验证通过'
        }
        return False, msg

    def send_email(self, request, reg_token):
        email = request.data.get('email')
        username = request.data.get('username')
        subject = '墨流引兮网站用户激活邮件'
        url = "http://127.0.0.1:8000/user/active/"+"?token="+reg_token
        message = '''
                你好{}！欢迎使用墨流引兮网站
                <div style='border:1px #396362'>
                    复制<h3>{}</h3>
                    或点击<a href='{}'>这里前往</a>激活用户
                </div>
            ''' .format(username, url, url)
        rel = send_mail(subject=subject, message='',
                        html_message=message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[email])
        return rel

    def make_token(self):
        token = uuid.uuid4().hex
        return token

    def username_exist(self, username):
        # 判断用户名是否存在于数据库
        user = FansUser.objects.filter(username=username).first()
        if user is not None:
            return user
        else:
            # 用户不存在
            return False


def user_active(request):
    token = request.GET.get('token')
    username = cache.get(token)
    user = FansUser.objects.filter(username=username).first()
    user.is_active = True
    user.save()
    return redirect(reverse('index:index'))


