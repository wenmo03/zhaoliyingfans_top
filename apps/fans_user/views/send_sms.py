import random

import requests
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SendSms(APIView):
    def get(self, request):
        """
        GET请求，用于验证短信验证码是否正确
        需要两个参数：
            code：验证码
            phone：手机号码
        :param request:
        :return:
        """
        code = request.query_params.get('code')
        phone = request.query_params.get('phone')
        if cache.get(phone) == code:
            data = {
                "status": status.HTTP_200_OK,
                "msg": "验证码验证成功"
            }
            return Response(data)
        else:
            data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "msg": "验证码验证失败"
            }
            return Response(data)

    def post(self, request):
        """
        POST请求，用于发送验证码
        需要传入一个参数：
            phone: 手机号
        :param request:
        :return:
        """
        phone = request.data.get('phone')
        vcode = self.gen_vcode(1000, 10000)

        cache.set(phone, vcode, 60 * 60)
        result = self.send_vcode(vcode, phone)
        return Response(result)

    def send_vcode(self, vcode, phone):
        """使用云之讯短信验证平台提供验证码发送服务ucpaas.com"""
        url = 'https://open.ucpaas.com/ol/sms/sendsms'

        querystring = {
            "sid": 'a88108ca93a370050637e49ec1c905de',
            "token": '730223d4cd49a0169ba5141e6d208cc6',
            "appid": '44b8828cb3aa408e9b8b74059d6f2f1b',
            "templateid": "487820",
            "param": str(vcode) + ',600',
            "mobile": phone,
        }

        response = requests.post(url, json=querystring)
        # print('return:', response)
        return response

    def gen_vcode(self, param, param1):
        return random.randint(param, param1)
