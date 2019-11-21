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
          "data": {
             "token": "token:12232sd",
             "last_login": "2019-12-01"
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
    ```
    
3. 用户激活邮件接口
    ```
    URL: '/u/active/'
    ```
    http请求方式：`POST` / `GET`
    
4. 用户名唯一验证：
    ```
    URL: '/u/usernameOnly/'
    ```
5. 第三方登录(微博登录接口)：
    ```
    URL: '/u/weibo_login/'
    ```
