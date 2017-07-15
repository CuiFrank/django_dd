from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from df_user.models import *
from goods.models import *
from user_center.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db import transaction
import json
import time
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

    ids_str = request.COOKIES.get('ids_str', '')
    ids = ids_str.split(',')[:-1]
    goods_list = []
    for i in ids:

        goods = GoodsInfo.objects.get(pk=int(i))
        goods_list.append(goods)


    if ucode != '':
        user = UserInfo.objects.get(id=int(ucode))



        context = {'title': '用户中心-天天生鲜', 'first_line': '1',
                   'second_line': '1','user': user, 'list':list, 'goods_list':goods_list}


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
        main_order = OrderMainInfo.objects.filter(user=user)
        main_detail = []
        for main in main_order:
            detail = OrderDetailInfo.objects.filter(order=main)
            main_detail.append({'main':main,'detail':detail})
        print(main_detail)
        context = {'title': '全部订单-天天生鲜', 'first_line': '1','second_line': '1',
                   'user':user, 'main_detail':main_detail, }
        return render(request, 'user_center/user_center_order.html', context)
    else:
        return redirect('/user/login/')



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


@login_decorate
def cart(request, ucode):
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


def is_login(request):
    value = request.COOKIES.get('isLogin', '')
    if value == '':
        return JsonResponse({'res': 'no'})
    else:
        return JsonResponse({'res': 'yes'})


def add_cart(request):
    get_value = request.GET
    try:
        name = request.session['name']
        num = get_value.get('num', 0)
        bao = get_value.get('bao', 0)
    except:
        return redirect('/user/login/')
    else:
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
    print('haha')
    return JsonResponse({'res':'ok'})


def checked(request):
    gid = request.GET.get('gid')
    name = request.session['name']
    if name != '':
        user = UserInfo.objects.get(name=name)
        cart = CartInfo.objects.filter(user=user).filter(id=int(gid))
        c = cart[0]
        c.isDelete = True
        c.save()
        print(c.isDelete)
        return JsonResponse({'res':'ok'})


def place_order(request):
    name = request.session['name']
    cart_list = request.POST.getlist('left_check')
    cart_list2 = []
    cart_ids = ','.join(cart_list)
    for c in cart_list:
        cart = CartInfo.objects.get(id=c)
        cart_list2.append(cart)
    if name != '':
        user = UserInfo.objects.get(name=name)
        context = {'title':'提交订单-天天生鲜', 'first_line':'1', 'location':'2',
                   'user':user, 'cart_list2':cart_list2,
                   'cart_ids':cart_ids, }
        return render(request, 'user_center/place_order.html', context)


def cart_add_one(request):
    count_one = request.POST.get('count_one')
    tot_one = request.POST.get('tot_one')
    gid = request.POST.get('gid')
    print(gid)
    c = CartInfo.objects.get(id=int(gid))
    c.num = int(count_one)
    c.total = float(tot_one)
    c.save()
    return JsonResponse({'res':'ok'})


@csrf_exempt
@transaction.atomic
def sub_order(request):
    sid = transaction.savepoint()
    is_fail = False
    try:
        main_order = OrderMainInfo()
        name = request.session.get('name')
        user = UserInfo.objects.get(name=name)
        main_order.user = user
        str_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        main_order.order_serial = str_now + str(user.id)
        main_order.state = 0
        main_order.address = request.POST.get('address')
        main_order.save()
        cart_list = request.POST.get('cart_ids').split(',')
        total = 0
        num = 0
        for cart in cart_list:
            goods_cart = CartInfo.objects.get(id=int(cart))
            detail_order = OrderDetailInfo()
            detail_order.order = main_order
            goods = GoodsInfo.objects.get(id=goods_cart.goods_id)
            detail_order.goods = goods
            detail_order.count = goods_cart.num
            detail_order.price = goods_cart.price
            detail_order.tot_one = goods_cart.num * goods_cart.price
            total += goods_cart.num * goods_cart.price
            num += 1
            detail_order.save()

            if goods_cart.num > goods.rest:
                is_fail = True
                print('nononononono')
            else:
                goods.rest -= goods_cart.num
                print('buy buy buy')

                goods.save()
            goods_cart.delete()
        main_order.total = total
        main_order.num = num
        main_order.save()

    except Exception as e:
        transaction.savepoint_rollback(sid)
        print('rollroll2')
        res = 'no'
    else:
        if is_fail:
            transaction.savepoint_rollback(sid)
            print('rollroll1')
            res = 'no'
        else:
            transaction.savepoint_commit(sid)
            print('yesyes1')
            res = 'ok'
    return JsonResponse({'res': res})


