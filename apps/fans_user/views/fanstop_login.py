from django.contrib.auth.hashers import check_password
from django.core.cache import cache

from fans_user.custom_tools import CustomTools

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fans_user.models import UserOfFans


class FansTopLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = UserOfFans.objects.filter(username=username).first()
        tool = CustomTools()
        token = tool.make_token()
        cache.set(token, username, 60 * 60 * 24)
        if check_password(password, user.password):

            if not user.is_active:
                data = {
                    "status": status.HTTP_202_ACCEPTED,
                    'msg': '当前用户还没有激活',
                    "data": {
                        'username': user.username,
                        'email': user.email,
                        'token': token
                    }
                }
                return Response(data)

            data = {
                'status': status.HTTP_200_OK,
                'msg': '登陆成功',
                'token': token,
                'data': {
                    'flag': 'fans',
                    "username": username
                }
            }
            return Response(data)
        else:
            data = {
                'satus': status.HTTP_400_BAD_REQUEST,
                'msg': 'PassWord Error',
            }
            return Response(data)
