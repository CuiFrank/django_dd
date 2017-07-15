from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from df_user.models import *


# Create your views here.


def index(request):
    kinds = KindsInfo.objects.all()
    list1 = []

    for kind in kinds:
        newlist = kind.goodsinfo_set.order_by('-id')[0:4]
        clicklist = kind.goodsinfo_set.order_by('click')[0:4]
        list1.append({'newlist': newlist, 'clicklist': clicklist, 't1': kind, })

    try:
        name = request.session['name']
        user = UserInfo.objects.get(name=name)
        cartlist = CartInfo.objects.filter(user=user)
        # 获取购物车中物品的数量
        tot_num = 0
        for cart_good in cartlist:
            tot_num += cart_good.num

    except:
        context = {'list1':list1,'tot_num': 0,'title': '首页', 'first_line': '1', 'second_line': '2'}
    else:
        context = {'list1':list1, 'tot_num': tot_num, 'title': '首页','first_line': '1', 'second_line': '2'}
    return render(request, 'index/index.html', context)


def list(request, uid, pindex, orderby):
    # kinds = KindsInfo.objects.all()
    # list2 = []
    # for kind in kinds:
    #     newlist = kind.goodsinfo_set.order_by('-id')[0:2]
    #     goodslist = kind.goodsinfo_set.order_by('-id')
    #     list2.append({'newlist':newlist, 'goodslist':goodslist, 't2':kind})

    desc = 1
    kind = KindsInfo.objects.get(id=uid)
    newlist = kind.goodsinfo_set.order_by('-id')[0:2]
    goodslist = ''
    if(orderby == '1'):
        goodslist = kind.goodsinfo_set.order_by('-id')

    elif (orderby == '2'):
        desc = request.GET.get('desc')
        if desc == '1':
            goodslist = kind.goodsinfo_set.order_by('-price')
        else :
            goodslist = kind.goodsinfo_set.order_by('price')

    elif (orderby == '3'):
        goodslist = kind.goodsinfo_set.order_by('click')


    paginator = Paginator(goodslist, 2)

    if pindex == '':
        pindex = 1
    page = paginator.page(int(pindex))

    last_index = page.paginator.page_range[-1]

    context = { 'newlist':newlist, 'orderby':orderby, 'desc':desc,'uid':uid,'kind':kind,'page':page,
                'last_index':last_index,
                'title': '列表','first_line': '1', 'second_line': '2',
                'third_l': '3', 'navbar': '4'}
    return render(request, 'index/list.html', context)


def detail(request, type, uid):
    try:
        good = GoodsInfo.objects.get(id=uid)
        good.click += 1
        good.save()
        kind = KindsInfo.objects.get(id=type)
        newlist = kind.goodsinfo_set.order_by('-id')[0:2]
        context = {'title': '商品详情-天天生鲜',
                   'good':good, 'newlist':newlist,
                   'first_line': '1', 'second_line': '2'}
        response = render(request, 'index/detail.html', context)

        ids_str = request.COOKIES.get('ids_str', '')
        ids = ids_str.split(',')
        if uid not in ids:
            ids.insert(0,uid)
        length = len(ids)
        if length>6:
            ids.pop()
        ids_str = (',').join(ids)
        response.set_cookie('ids_str', ids_str, max_age=60*60*24*7)
        return response
    except:
        return render(request,'404.html')




