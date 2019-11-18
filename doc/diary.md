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
