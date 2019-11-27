## 用户相关接口
1. 原生用户登录接口
    ``` 
    URL:    /u/sign_in/
    ```
     用户可以使用在本网站注册的用户名和密码进行登录 
     
     http请求方式：`POST`
     
     需要提交的字段
    
    |  |必选| 类型| 说明|
    |-----|---|----|----|
    |username|ture|string|用户名|
    |password|ture|string|密码|
    
    返回数据
    ```json
        {
          "status": 200,
          "msg": "登录成功",
          "token": "TOKEN",
          "data": {
             "flag": "fans",
             "username": "USERNAME" 
          }    
        }
    ```
    用户未激活登录失败
    ```
        {
            "status": 202,
            'msg': '当前用户还没有激活',
            "data": {
                'username': "USERNAME",
                'email': "EMAIL",
                'token': "TOKEN"
            }
         }
   ```
2. 原生用户注册接口
    ```
    URL: '/u/sign_up/'
    ```
    
    http请求方式：`POST`
    
    需要提交的字段
    
    |  |必选| 类型| 说明|
    |-----|---|----|----|
    |username|ture|string|用户名|
    |password|ture|string|密码|
    |repassword|true|string|重复密码|
    |email|True|string|邮箱|
    
    返回数据
    
    请求成功：    
    ```json
    {
    "status": 201,
    "msg": "success",
    "token": "4d40f01bfcd047cfad619f41ade20fdf",
    "data": {
        "username": "USERNAME",
        "email": "USER_EMAIL"
        }
    }
    ```
    
3. 用户激活邮件接口
    ```
    URL: '/u/active/'
    ```
    http请求方式：`POST` / `GET`
    1. `GET`请求
        
        |  |必选| 类型| 说明|
        |-----|---|----|----|
        |token|ture|string|用户token|
        
        返回数据
        
        ```json
           {
            "status": 200,
            "msg": "用户激活成功",
            "data": {
                    "username": "USERNAME",
                    "active_status": "active"
                }
        }
        ```
    2. `POST` 请求
        
       |  |必选| 类型| 说明|
        |-----|---|----|----|
        |token|ture|string|用户token|
        |email|true|string|用户邮箱|
       返回数据
       ```json
         {
                "status": "HTTP_200_OK",
                "msg": "邮件已发送"
         }
        ```
4. 用户名唯一验证：
    ```
    URL: '/u/usernameOnly/'
    ```
5. 第三方登录(网站微博登录接口)：
    ```
    URL: '/u/weibo_login/'
    ```
    
    HTTP请求方式：`GET`
    
    ```json
     {
    "status": 200,
    "msg": "微博登录成功",
    "user": {
        "flag": "weibo",
        "uid": "5782250369",
        "nickname": "墨流引",
        "token": "2.00j9j__GSwSE5B517e088243n8kREE"
         }
    }
    ```
6. 短信验证码接口   
    ```
    URL: /u/send_msg/
    ```
    
    http请求方式：`POST` / `GET`
    
    1. `GET`请求(用于验证短信验证码是否正确)
    
        |  参数|必选|说明|
        |:------:|:-----:|:----:|
        |code|必填|验证码|
        |phone|必填|手机号码(用于接受验证码)|
        
        返回数据
        ```
        # 成功
            {
                "status": 200,
                "msg": "验证码验证成功"
            }
        # 失败
            {
                "status": 400,
                "msg": "验证码验证失败"
            }
        ```
    
    2. `POST`请求(用于发送短信验证码)
        
         |  参数|必选|说明|
        |:------:|:-----:|:----:|
        |phone|必填|手机号码(用于接受验证码)|
        
        ```
        # 返回结果
        
            {
               "code":"0",
               "msg":"OK", 
               "count":"1",
               "create_date":"2017-08-28 19:08:28",
               "smsid":"f96f79240e372587e9284cd580d8f953",
               "mobile":"18011984299",
               "uid":"2d92c6132139467b989d087c84a365d8"
            }
        ```
        
    
 