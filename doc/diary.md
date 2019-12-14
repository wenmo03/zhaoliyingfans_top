## setting.py

mysql数据库配置
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fans_db',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': 3306
    }
}
```
配置Redis缓存
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',  # 'redis://:你的密码@redis数据库服务器的地址:6379/0'
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}
REDIS_TIMEOUT = 7*24*60*60
CUBES_REDIS_TIMEOUT = 60*60
NEVER_REDIS_TIMEOUT = 365*24*60*60
```
配置时区
```python
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False
```
配置静态文件夹
```python
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/static/media/'
MEDIA_ROOT = [os.path.join(BASE_DIR,'static/media')]
```

配置包根目录
```
sys.path.insert(0,os.path.join(BASE_DIR, 'apps'))
# 打包已安装的python扩展
pip freeze | tee requirements.txt
# OR
pip freeze > requirements.txt
```


## 报错
django 2.2 报错
```
LookupError: No installed app with label 'admin'.
```
解决尝试
```
pip install sqlparse # 失败
pip install pymysql  # 失败
pip install django==2.0 # 降低版本，错误解决，什么垃圾2.2我不用了还不行吗
```

## 警告
django 2.0 存在漏洞
```
1.11.19之前的Django 1.11.x，2.0.11之前的2.0.x和2.1.6之前的2.1.x允许通过恶意的攻击者提供的值对django.utils.numberformat.format（）函数进行不受控制的内存消耗。
Django 2.0中2.0.2以及1.11.8和1.11.9之前的django.contrib.auth.forms.AuthenticationForm允许远程攻击者通过利用来自verify_login_allowed（）方法的数据暴露来获取潜在的敏感信息，这通过发现是否用户帐户无效。
```

建议升级：django> = 2.0.11
## 第三方登录
```
pip install django-allauth
```

```python
# 微博登录
# 文档 https://open.weibo.com/wiki/Oauth2/authorize
# 获取登录接口API
# 'https://api.weibo.com/oauth2/authorize?client_id='
# 获取用户token和uid
# "https://api.weibo.com/oauth2/access_token"
# 获取退出登录
# 'https://api.weibo.com/oauth2/revokeoauth2'
```

解决跨域问题。在后端Django项目demo2中安装相关模块：

pip install Django-cors-headers


然后在settings.py中的注册里配置如下：

```
INSTALLED_APPS = [
    'Django.contrib.admin',
    'Django.contrib.auth',
    'Django.contrib.contentTypes',
    'Django.contrib.sessions',
    'Django.contrib.messages',
    'Django.contrib.staticfiles',
    'app01.apps.App01Config',
    'rest_framework',
    'corsheaders'
]
```

在settings.py中的MIDDLEWARE里设置如下：

```
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',                            #放到中间件顶部
    'Django.middleware.security.SecurityMiddleware',
    'Django.contrib.sessions.middleware.SessionMiddleware',
    'Django.middleware.common.CommonMiddleware',
    'Django.middleware.csrf.CsrfViewMiddleware',
    'Django.contrib.auth.middleware.AuthenticationMiddleware',
    'Django.contrib.messages.middleware.MessageMiddleware',
    'Django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

在settings.py中新增配置项，即可解决本项目中的跨域问题。
```
CORS_ORIGIN_ALLOW_ALL = True
```
注意：在Python全栈开发的知识体系里，跨域问题和深浅拷贝，几乎是逢面试必考的两个笔试题。不同的是，深浅拷贝在实际项目中很少用到，而跨域问题却几乎在每个项目中都有涉及，只是并非都能被察觉罢了。跨域问题是非常重要的一个知识点，关系到网络安全，甚至说跨域问题是Web安全中最重要的一环也不为过。

### DRF分页
普通分页
```
# setting.py设置

```
REST_FRAMEWORK = {
    'PAGE_SIZE': 3
}

```
# APIView使用分页
    # 查出所有数据
    blog_data = Blog.objects.all()
    # 2、创建分页对象
    pg = PageNumberPagination()
    # 3、将数据库中的数据进行分页处理
    page_blog = pg.paginate_queryset(queryset=blog_data, request=request, view=self)
    # 4、序列化分页后的对象
    blog_serializers = SerializerBlog(page_blog, many=True)
```
然后请求接口，就会默认以每页三个数据显示
` /blog/rank/?page=2` 可以通过传入page参数来访问指定页。
