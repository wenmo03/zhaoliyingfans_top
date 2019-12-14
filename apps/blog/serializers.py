from rest_framework import serializers

from blog.models import Blog


class SerializerBlog(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['b_title', 'b_content', 'b_user']
