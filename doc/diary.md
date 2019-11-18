setting.py

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
```
pip freeze | tee requirements.txt
# OR
pip freeze > requirements.txt
```

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
