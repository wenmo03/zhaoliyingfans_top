# Generated by Django 2.0.12 on 2019-11-22 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fans_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOfWeibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=64, null=True)),
                ('nickname', models.CharField(blank=True, max_length=128, null=True, verbose_name='昵称')),
                ('head', models.CharField(blank=True, max_length=232, null=True, verbose_name='头像50')),
                ('head_large', models.CharField(blank=True, max_length=232, null=True, verbose_name='头像180')),
                ('description', models.TextField(blank=True, null=True, verbose_name='用户简介')),
                ('sex', models.CharField(blank=True, max_length=16, null=True, verbose_name='性别')),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('is_delete', models.BooleanField(default=False, verbose_name='用户是否被禁用')),
            ],
            options={
                'db_table': 'user_of_weibo',
            },
        ),
        migrations.RemoveField(
            model_name='useroffans',
            name='description',
        ),
        migrations.RemoveField(
            model_name='useroffans',
            name='sex',
        ),
        migrations.AddField(
            model_name='userofweibo',
            name='user_of_fans',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fans_user.UserOfFans'),
        ),
    ]