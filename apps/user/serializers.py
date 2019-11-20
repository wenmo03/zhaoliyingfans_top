from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.models import FansUser


class FansUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FansUser
        fields = ['username', 'nickname', 'email', 'wb_id', 'head']


class RegisterFansUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FansUser
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        username = validated_data.get('username')
        pwd = validated_data.get('password')
        email = validated_data.get('email')
        password = make_password(pwd)
        # print(validated_data, email, pwd, password, username)
        user = FansUser.objects.create(username=username, password=password, email=email)
        return user
