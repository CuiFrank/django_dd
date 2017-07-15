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



