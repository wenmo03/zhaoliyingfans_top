from django.core.cache import cache
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fans_user.models import UserOfFans
from zhaoliyingfans_top import settings


class ActiveCode(APIView):
    def get(self, request):
        token = request.query_params.get('token')
        username = cache.get(token)
        user = UserOfFans.objects.filter(username=username).first()
        if user:
            user.is_active = True
            user.save()
            data = {
                'status': status.HTTP_200_OK,
                'msg': '用户激活成功',
                'data': {
                        'username': username,
                        'active_status': 'active',
                    }
            }
            return Response(data)
        else:
            data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '用户激活失败',
            }
            return Response(data)

    def post(self, request):
        reg_token = request.data.get('token')
        rel = self.send_email(request, reg_token)
        if rel:
            data = {
                "status": status.HTTP_200_OK,
                "msg": "邮件已发送",
            }
            return Response(data)
        else:
            data = {
                "status": status.HTTP_204_NO_CONTENT,
                "msg": "邮件发送失败",
            }
            return Response(data)

    def send_email(self, request, reg_token):
        email = request.data.get('email')
        username = cache.get(reg_token)
        subject = '墨流引兮网站用户激活邮件'
        url = "http://127.0.0.1:8000/u/active/"+"?token="+reg_token
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


class UsernameOnly(APIView):
    def get(self, request):
        pass