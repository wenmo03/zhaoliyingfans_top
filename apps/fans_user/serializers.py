from django.contrib.auth.hashers import make_password

from fans_user.models import UserOfFans
from rest_framework import serializers


class SerializerUserOfFans(serializers.ModelSerializer):
    class Meta:
        model = UserOfFans
        fields = ['username', 'password', 'email']

    def create(self, validated_data):

        pwd = validated_data.get('password')
        validated_data['password'] = make_password(pwd)
        user = UserOfFans.objects.create(**validated_data)
        return user