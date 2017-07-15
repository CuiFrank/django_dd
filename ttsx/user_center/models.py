from django.db import models
from goods.models import *
from df_user.models import *


class OrderMainInfo(models.Model):
    order_serial = models.CharField(max_length=24,null=True)
    user = models.ForeignKey(UserInfo)
    address = models.CharField(max_length=100)
    order_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(null=True)
    num = models.IntegerField(null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2,null=True)


class OrderDetailInfo(models.Model):
    order = models.ForeignKey('OrderMainInfo')
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    tot_one = models.DecimalField(max_digits=10,decimal_places=2, null=True)