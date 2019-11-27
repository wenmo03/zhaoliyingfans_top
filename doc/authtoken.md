（1）安装Django REST framework及其依赖包markdown和django-filter。

```
pip install djangorestframework markdown Django-filter
```

（2）在settings.py中添加注册代码：
```
INSTALLED_APPS = [
    'Django.contrib.admin',
    'Django.contrib.auth',
    'Django.contrib.contenttypes',
    'Django.contrib.sessions',
    'Django.contrib.messages',
    'Django.contrib.staticfiles',
    'app01.apps.App01Config',
    'rest_framework',
    'rest_framework.authtoken'
]
```

（3）打开终端，执行数据更新命令：

```
Python manage.py makemigrations
Python manage.py migrate
```

上一节我们已经通过对demo5的改造，成功生成并且获取到了Token，接下来开发Token认证的功能，步骤如下：

（1）在settings.py中添加配置代码：
```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',                   #必须有
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
```
注意：上述代码中，在settings中不但要加入认证的配置代码，还要加入权限的配置代码，如果不加入权限的配置代码，那么认证代码将无法阻止未认证用户获取到本应该只有已认证的用户才可以获取到的数据信息，这一点与Django REST framework的官方文档存在差异，有可能是因为版本问题而产生的Bug。

（2）将app01/views.py中的代码重写为：
```
from Django.shortcuts import render,redirect,HttpResponse
from rest_framework.views import APIView
# Create your views here.
class IndexView(APIView):
    """
    首页
    """
    # authentication_classes = []
    # permission_classes = []
    def get(self,request):
        # print(request)
        return HttpResponse('首页')
```
（3）将urls.py中的代码重写为：
```
from Django.contrib import admin
from Django.urls import path
from rest_framework.authtoken import views
from app01.views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
 ```
drf自带的token认证模式

```
path('api-token-auth/', views.obtain_auth_token),
path('index/',IndexView.as_view(),name='index'),
]
```

（4）运行项目demo5，然后使用Postman在协议头中加入键值对：
```
{
“Authorization”:” Token a8c033e6facb3acce67ab26d341b8b3240619715”
}
```
注意：Token与字符串之间有一个空格。

运行效果如图5-22所示。

（5）如果Token信息不正确，则会返回以下内容，如图5-23所示。
```
{
  "detail": "Authentication credentials were not provided."
}
```