from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog
from blog.serializers import SerializerBlog


class BlogAPIView(APIView):
    def get(self, request):

        blog_data = Blog.objects.all()
        # 2、创建分页对象
        pg = PageNumberPagination()
        # 3、将数据库中的数据进行分页处理
        page_blog = pg.paginate_queryset(queryset=blog_data, request=request, view=self)
        # 4、序列化分页后的对象
        blog_serializers = SerializerBlog(page_blog, many=True)

        data = {
            'status': '2000',
            'msg': 'Get Success',
            'data': blog_serializers.data,
        }
        return Response(data)

    def post(self, request):

        blog_serializers = SerializerBlog(data=request.data)
        # print(request.data)
        # print(blog_serializers.is_valid())
        if blog_serializers.is_valid():
            blog_serializers.save()

            data = {
                'status': '2000',
                'msg': 'Post Success'
            }
            return Response(data)
        else:
            return Response({"error": "ERROR: Please check your data"})
