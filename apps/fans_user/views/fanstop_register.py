import uuid

from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fans_user.custom_tools import CustomTools
from fans_user.models import UserOfFans
from fans_user.serializers import SerializerUserOfFans


class FansTopRegister(APIView):
    def post(self, request):
        reg_result = self.do_register(request)
        if reg_result[0]:
            return Response(reg_result[1])

        fans_user_serializers = SerializerUserOfFans(data=request.data)
        if fans_user_serializers.is_valid():
            fans_user_serializers.save()

        # 激活注册用户，token有效期一小时
        tool = CustomTools()
        token = tool.make_token()
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

    def username_exist(self, username):
        # 判断用户名是否存在于数据库
        user = UserOfFans.objects.filter(username=username).first()
        if user is not None:
            return user
        else:
            # 用户不存在
            return False

