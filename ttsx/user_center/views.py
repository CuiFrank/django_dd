from django.shortcuts import render

# Create your views here.


def cart(request):
    return render(request, 'user_center/cart.html', {'title':'天天生鲜-购物车'})


def user_center_info(request):
    return render(request, 'user_center/user_center_info.html', {'title':'天天生鲜-用户中心'})


def user_center_site(request):
    return render(request, 'user_center/user_center_site.html',{'title':'天天生鲜-收货地址'})


def user_center_order(request):
    return render(request, 'user_center/user_center_order.html', {'title':'天天生鲜-全部订单'})


def place_order(request):
    return render(request, 'user_center/place_order.html',{'title':'天天生鲜-提交订单'})
