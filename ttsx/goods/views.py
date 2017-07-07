from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    kinds = KindsInfo.objects.all()
    list1 = []
    for kind in kinds:
        newlist = kind.goodsinfo_set.order_by('-id')[0:4]
        clicklist = kind.goodsinfo_set.order_by('click')[0:4]
        list1.append({'newlist':newlist,'clicklist':clicklist, 't1':kind})
    context = {'list1':list1, 'title': '首页','first_line': '1'}
    return render(request, 'index/index.html', context)
















def detail(request):
    return render(request, 'goods/detail.html', {'title': '天天生鲜-商品详情'})


def list(request):
    return render(request, 'goods/list.html', {'title': '天天生鲜-商品列表'})