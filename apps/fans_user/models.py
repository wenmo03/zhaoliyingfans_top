from django.db import models

# Create your models here.


class UserOfFans(models.Model):
    username = models.CharField(max_length=64, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=232, verbose_name='密码')
    email = models.CharField(max_length=232, verbose_name='邮箱', null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    sex = models.CharField(max_length=16, null=True, blank=True, verbose_name='性别')
    register_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    register_ip = models.CharField(max_length=32, null=True, blank=True, verbose_name='注册IP')
    last_update = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')
    description = models.TextField(null=True, blank=True, verbose_name='用户简介')
    is_active = models.BooleanField(default=False, verbose_name='用户是否激活')
    is_delete = models.BooleanField(default=False, verbose_name='用户是否被禁用')

    class Meta:
        db_table = 'user_of_fans'


# class UserOfWeibo(models.Model):
#     uid = models.CharField(max_length=64, null=True, blank=True)
#     nickname = models.CharField(max_length=128, verbose_name='昵称', null=True, blank=True)
#     head = models.CharField(max_length=232, null=True, blank=True)
#     user_of_fans = models.OneToOneField(to=UserOfFans, on_delete=models.SET_NULL, null=True, blank=True)
#
#     class Meta:
#         db_table = 'user_of_weibo'
