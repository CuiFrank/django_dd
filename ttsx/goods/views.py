from django.shortcuts import render

# Create your views here.


def detail(request):
    return render(request, 'goods/detail.html', {'title': '天天生鲜-商品详情'})


def list(request):
    return render(request, 'goods/list.html', {'title': '天天生鲜-商品列表'})