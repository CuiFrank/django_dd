from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from df_user.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def login_decorate(func):
    def inner(request, *args, **kwargs):
        if 'isLogin' in request.COOKIES:
            ucode = request.COOKIES.get('isLogin','')
            return func(request, ucode)
        else:
            return redirect('/user/login/')
    return inner


def cart(request):
    return render(request, '/user_center/cart.html', {'title':'天天生鲜-购物车'})


@login_decorate
def user_center_info(request, ucode):
    # uid = request.session.get(ucode)
    list = request.session['name']
    if ucode != '':
        user = UserInfo.objects.get(id=int(ucode))
        context = {'title': '用户中心-天天生鲜', 'first_line': '1', 'user': user, 'list':list}
        return render(request, 'user_center/user_center_info.html', context)
    else:
        return redirect('/user/login/')


@login_decorate
def user_center_site(request, ucode):
    if ucode != '':
        user = UserInfo.objects.get(id=int(ucode))
        name = user.name
        if name in request.session:
            site = request.session[name]
        else:
            site = ''
        # msg = name + '&nbsp;'+ user.address +'&nbsp;'+user.code +'&nbsp;'+user.phone

        context = {'title': '收货地址-天天生鲜', 'first_line': '1', 'user': user}
        return render(request, 'user_center/user_center_site.html', context)
    else:
        return redirect('/user/login/')


@login_decorate
def user_center_order(request, ucode):
    if ucode != '':
        user = UserInfo.objects.get(id=int(ucode))
        context = {'title': '全部订单-天天生鲜', 'first_line': '1', 'user':user}
        return render(request, 'user_center/user_center_order.html', context)
    else:
        return redirect('/user/login/')


@csrf_exempt
def post_site(request):
    # rman = request.POST.get('receive_man')
    # rarea = request.POST.get('receive_area')
    # rcode = request.POST.get('receive_code')
    # rphone = request.POST.get('receive_phone')
    rman = request.POST.get('rman')
    rarea = request.POST.get('rarea')
    rcode = request.POST.get('rcode')
    rphone = request.POST.get('rphone')


    u = UserInfo.objects.get(name=rman)
    u.address = rarea
    u.code = rcode
    u.phone = rphone
    u.save()


    return JsonResponse({'res': 'ok'})
    # return redirect('/center/user_center_site/')


def place_order(request):
    return render(request, 'user_center/place_order.html',{'title':'天天生鲜-提交订单'})


