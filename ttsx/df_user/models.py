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

