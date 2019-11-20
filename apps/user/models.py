from django.db import models

# Create your models here.


class FansUser(models.Model):
    username = models.CharField(max_length=64, verbose_name='用户名', null=True, blank=True)
    nickname = models.CharField(max_length=128, verbose_name='昵称', null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name='邮箱', null=True, blank=True)
    password = models.CharField(max_length=200, verbose_name='密码', null=True, blank=True)
    wb_id = models.CharField(max_length=64, null=True, blank=True)  # 微博关联的id
    head = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=16, null=True, blank=True)
    register_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    register_ip = models.CharField(max_length=32, null=True, blank=True)
    last_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fans_user'

# https://api.weibo.com/oauth2/authorize?client_id=2239662307&redirect_uri=http://www.example.com/response&response_type=code


