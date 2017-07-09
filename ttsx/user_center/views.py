from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from df_user.models import *
from goods.models import *
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


@login_decorate
def user_center_info(request, ucode):
    # uid = request.session.get(ucode)
    list = request.session['name']
    if ucode != '':
        user = UserInfo.objects.get(id=int(ucode))
        context = {'title': '用户中心-天天生鲜', 'first_line': '1', 'second_line': '1','user': user, 'list':list}
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

        context = {'title': '收货地址-天天生鲜', 'first_line': '1','second_line': '1', 'user': user}
        return render(request, 'user_center/user_center_site.html', context)
    else:
        return redirect('/user/login/')


@login_decorate
def user_center_order(request, ucode):
    if ucode != '':
        user = UserInfo.objects.get(id=int(ucode))
        context = {'title': '全部订单-天天生鲜', 'first_line': '1','second_line': '1', 'user':user}
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


def cart(request):
    name = request.session['name']
    u = UserInfo.objects.get(name=name)
    cartlist_raw = CartInfo.objects.filter(user=u)
    num = cartlist_raw.count()
    tot = 0.00
    # 将购物车中的查询集遍历放在列表中返回，因为查询集无法直接返回给模板
    cartlist = []
    # 总件数为tot_num
    tot_num = 0

    for cart_good in cartlist_raw:

        # 根据购物车保存的物品的id获取物品goodsinfo的库存，并添加到库存列表，传递给模板
        g = GoodsInfo.objects.get(id=cart_good.goods_id)
        r = g.rest
        cartlist.append({'cart_good':cart_good, 'rest':r})
        tot_num += cart_good.num

    # 查询出购物车中每种商品的总价，计算总和，返回给模板
    for m in cartlist:
        tot += float(m['cart_good'].total)
    context = {'cartlist':cartlist, 'num':tot_num,'tot': round(tot,2), 'title': '购物车-天天生鲜', 'first_line': '1',
               'second_line': '1', 'location': '1',}
    return render(request, 'user_center/cart.html', context)


def add_cart(request):
    get_value = request.GET
    name = request.session['name']
    num = get_value.get('num', 0)
    bao = get_value.get('bao', 0)
    c = CartInfo()
    u = UserInfo.objects.get(name=name)
    b = GoodsInfo.objects.get(id=int(bao))
    c.title = b.title
    c.pic = b.pic
    c.price = b.price
    c.unit = b.unit
    c.num = num
    c.total = round(float(b.price),2)*int(num)
    c.user = u
    c.goods_id = b.id
    c.save()
    return JsonResponse({'res':'ok'})

def cart_del(request):
    get_value = request.GET
    gid = get_value.get('gid')

    g = CartInfo.objects.get(id=int(gid))
    g.delete()
    return JsonResponse({'res':'ok'})



def place_order(request):
    return render(request, 'user_center/place_order.html',{'title':'天天生鲜-提交订单'})


