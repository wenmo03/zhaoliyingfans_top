from django.urls import path

from blog.views import BlogAPIView
app_name = 'blog'

urlpatterns = [
    path('rank/', BlogAPIView.as_view(), name='rank'),
]