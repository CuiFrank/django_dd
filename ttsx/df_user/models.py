from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=40)
    e_mail = models.CharField(max_length=20)
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=11, default='')
    code = models.CharField(max_length=6, default='')


class PostInfo(models.Model):
    post_addr = models.CharField(max_length=100, default='')
    post_phone = models.CharField(max_length=11, default='')
    post_code = models.CharField(max_length=6, default='')

    post_name = models.ForeignKey(UserInfo)


class CartInfo(models.Model):
    title = models.CharField(max_length=100, null=True)
    pic = models.ImageField(upload_to='goods/', default='')
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    unit = models.CharField(max_length=20, null=True)
    isDelete = models.BooleanField(default=False)
    num = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey('UserInfo')
    goods_id = models.IntegerField(default=200)
