````
def send_email(self, request):
    email = request.data.get('email')
    username = request.data.get('username')
    subject = '墨流引兮网站用户激活邮件'
    url = ''
    message = '''
            你好{}！欢迎使用墨流引兮网站
            <div style='border:1px #396362'>
                复制<h3>{}</h3>
                或点击<a href='{}'>这里前往</a>激活用户
            </div>
        ''' .format(username, url, url)
    rel = send_mail(subject=subject, message='', html_message=message, from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[email])
    return rel
````