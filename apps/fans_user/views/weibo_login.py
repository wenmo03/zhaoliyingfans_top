import json
import time

import requests
from django.core.cache import cache
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fans_user.models import UserOfWeibo
from zhaoliyingfans_top import settings


class WeiBoLogin(APIView):
    def get(self, request):
        app_id = settings.WEIBO_APP_ID
        re_url = settings.WEIBO_REDIRECT_URI
        url = 'https://api.weibo.com/oauth2/authorize?client_id={}&redirect_uri={}'.format(app_id, re_url)
        return HttpResponseRedirect(url)


class WeiBoGetCode(APIView):
    def get(self, request):
        """登录之后，跳转到这里。需要判断code和state"""
        code = request.GET.get('code', None)
        sina = OAuthWB(settings.WEIBO_APP_ID,
                       settings.WEIBO_APP_KEY,
                       settings.WEIBO_REDIRECT_URI)
        user_info = sina.get_access_token(code)
        # print(user_info)
        access_token = user_info['access_token']
        uid = user_info['uid']
        cache.set(access_token, uid, 60*60*24)

        # print(user_info)
        time.sleep(0.1)  # 防止还没请求到token就进行下一步
        # 通过uid查询出是否是新用户，新用户则注册登录
        is_user_exist = UserOfWeibo.objects.filter(uid=user_info['uid']).first()
        print('==============', is_user_exist, '====================')
        if is_user_exist is not None:
            # 存在直接登录
            data = {
                'status': status.HTTP_200_OK,
                'msg': '微博登录成功',
                'user': {
                    'flag': 'weibo',
                    'uid':  is_user_exist.uid,
                    'nickname': is_user_exist.nickname,
                    'token': access_token,
                }
            }
            return Response(data)
        else:
            # 不存在获取用户信息
            new_user_info = sina.get_user_info(user_info)
            users_dict = {
                "uid": new_user_info['id'],
                'description': new_user_info['description'],
                "head": new_user_info['profile_image_url'],
                "head_large": new_user_info['avatar_large'],
                "sex": new_user_info['gender'],
                "nickname": new_user_info['name'],
            }
            users_table_obj = UserOfWeibo.objects.create(**users_dict).id
            data = {
                'flag': 'weibo',
                'status': status.HTTP_200_OK,
                'msg': '微博登录成功',
                'user': {
                    'uid': users_table_obj.uid,
                    'nickname': users_table_obj.nickname,
                    'token': access_token,
                }
            }
            return Response(data)


class WeiboLogout(APIView):
    def get(self, request):
        url = 'https://api.weibo.com/oauth2/revokeoauth2'
        the_access_token = request.query_params.get('access_token')
        querystring = {
            "access_token": the_access_token
        }
        response = requests.request("GET", url, params=querystring)
        return HttpResponse(response)


class OAuthWB:
    def __init__(self, client_id, client_key, redirect_uri):
        self.client_id = client_id
        self.client_key = client_key
        self.redirect_uri = redirect_uri

    def get_access_token(self, code):  # 获取用户token和uid
        url = "https://api.weibo.com/oauth2/access_token"
        # 说明文档https://open.weibo.com/wiki/Oauth2/access_token
        querystring = {
            "client_id": self.client_id,
            "client_secret": self.client_key,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri
        }

        response = requests.request("POST", url, params=querystring)

        return json.loads(response.text)

    def get_token_info(self, access_token):
        # 查询用户access_token的授权相关信息，包括授权时间，过期时间和scope权限。
        url = 'https://api.weibo.com/oauth2/get_token_info'
        querystring = {
            'access_token': access_token
        }
        response = requests.request("POST", url, params=querystring)
        return json.loads(response.text)

    def get_user_info(self, access_token_data):
        url = "https://api.weibo.com/2/users/show.json"
        # 说明文档 https://open.weibo.com/wiki/2/users/show
        querystring = {
            "uid": access_token_data['uid'],
            "access_token": access_token_data['access_token']
        }

        response = requests.request("GET", url, params=querystring)

        return json.loads(response.text)

