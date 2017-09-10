from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import UserInfo
import hashlib
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.


def login(request):
    if 'name' in request.COOKIES:
        context = {'title': '登陆-天天生鲜', 'name': request.COOKIES['name'], 'first_line':0}
    else:
        context = {'title':'登陆-天天生鲜', 'first_line':0}
    return render(request, 'df_user/login.html', context)


def register(request):
    context = {'title':'注册-天天生鲜','first_line':0}
    return render(request, 'df_user/register.html', context)


@csrf_exempt
def register_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    else:
        name = request.GET.get('name')
    if UserInfo.objects.filter(name=name).count():
        return JsonResponse({'res': 0})
    else:
        return JsonResponse({'res': 1})


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upasswd = post.get('user_pwd')
    ue_mail = post.get('user_email')

    sha1 = hashlib.sha1()
    sha1.update(upasswd.encode())
    upasswd_sha1 = sha1.hexdigest()

    user = UserInfo()
    user.name = uname
    user.passwd = upasswd_sha1
    user.e_mail = ue_mail
    user.save()
    return redirect('/user/login/')


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upasswd = post.get('userpwd')
    remember = post.get('remember')
    user = UserInfo.objects.filter(name=uname)

    sha1 = hashlib.sha1()
    sha1.update(upasswd.encode())
    upasswd_sha1 = sha1.hexdigest()
    if len(user) == 0:
        return redirect('/user/login/')
    else:
        if user[0].passwd == upasswd_sha1:
            path = request.session.get('url_path', '')
            if path != '':
                # response = redirect('/center/user_center_info/')
                response = redirect(request.session['url_path'])
            else:
                response = redirect('/')
            request.session['name'] = user[0].name
            response.set_cookie('isLogin', user[0].id, expires=6000)

            if remember == '1':
                response.set_cookie('name', uname, expires=datetime.datetime.now()+datetime.timedelta(days=14))
            else:
                # request.session.flush()  #删除session表中的数据
                # del request.session[uname]
                response.set_cookie('name', uname, expires=-1)
            return response
        else:
            return redirect('/user/login/')


def logout(request):
    request.session.flush()
    response = redirect('/user/login/')
    response.set_cookie('isLogin', '',expires=-1)
    return response


# 发送邮件，需要导入的包


#from django.core.mail import send_mail,send_mass_mail
#from django.core.mail import EmailMultiAlternatives

'''
# 1.发送邮件的主题内容等
title='two email together'
message='Hello! This two message!'
#message.attach_alternative(html_content, "text/html")
sender='396524687@qq.com'
mail_list=['13423844632@163.com', '396524687@qq.com']

send_mail 使用

send_mail(subject=title,message=message,from_email=sender,recipient_list=mail_list,
            fail_silently=False,
            connection=None,
        )
'''

'''
# send_mass_mail 发送多个邮件，只建立一次连接，如果使用send_mail 则发送一个邮件建立一次连接，比较浪费资源
# 但收件人中所有人都会看见彼此的邮箱，如果想实现看不见，只能使用send_mail
        # 主题        内容                            发送者                收件者列表
message1=('f1','Hello! This is the first message!','396524687@qq.com',['13423844632@163.com', '396524687@qq.com'])
message2=('f2','Hello! This is the second message!','396524687@qq.com',['13423844632@163.com', '396524687@qq.com'])

send_mass_mail((message1,message2), fail_silently=False, auth_user=None, auth_password=None)

'''

'''
# 2.发送简单html，支持html则发送，不支持则为文本发送
from django.core.mail import EmailMultiAlternatives

subject = '来自自强学堂的问候'

text_content = '这是一封重要的邮件.'

html_content = '你好，世界'

msg = EmailMultiAlternatives(subject, text_content, '396524687@qq.com', bcc = ['396524687@qq.com','13423844632@163.com'],)

msg.attach_alternative(html_content, "text/html")

msg.send()
'''


# 3 用templates中的html发送，并添加附件
from django.core.mail import send_mail
from django.template import Context, loader

context = {
    # 'nickname': 'frank',
    # 'verify_url': 'http://127.0.0.1:8000/',
}
email_template_name = 'base.html'
t = loader.get_template(email_template_name)
mail_list = ['396524687@qq.com', '1342344632@163.com']
title = u'你好啊'
# EMAIL_HOST_USER = '相信自己'
# send_mail(
#     subject='你好',
#     message=t.render(Context(context)),
#     from_email= '396524687@qq.com',  # 发件邮箱
#     recipient_list=mail_list,
#     fail_silently=False,
#     # auth_user= '仪陇回程',  # SMTP服务器的认证用户名
#     # auth_password=EMAIL_HOST_PASSWORD,  # SMTP服务器的认证用户密码
#     connection=None
# )

from django.core.mail import EmailMultiAlternatives
from django.template import Context, loader

EMAIL_HOST_USER = '396524687@qq.com'

subject, from_email, to = title, EMAIL_HOST_USER, mail_list
html_content = t.render(Context(context))
msg = EmailMultiAlternatives(subject, html_content, from_email, to)
msg.attach_alternative(html_content, "text/html")

msg.attach_file(u'/home/python/Desktop/django-ttsx-704/django_ttsx/ttsx/static/images/adv01.jpg')
msg.send()




#　生成静态文件
from django.shortcuts import render
from django.template.loader import render_to_string
import os


def my_email(request):
    context = {'some_key': 'some_value'}

    static_html = 'base.html'

    if not os.path.exists(static_html):
        content = render_to_string('base.html', context)
        with open(static_html, 'w') as static_file:
            static_file.write(content)

    return render(request, static_html)
