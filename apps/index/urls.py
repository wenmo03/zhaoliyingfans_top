from django.urls import path

from apps.index.views import index
app_name = 'index'
urlpatterns = [
    path('', index, name='index'),
]