from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class KindsInfo(models.Model):
    kinds = models.CharField(max_length=20)
    rest = models.IntegerField()

    def __str__(self):
        return self.kinds


class GoodsInfo(models.Model):
#     # id, title, pic, price, select, unit, rest, sub_title, weight, detail
    title = models.CharField(max_length=100, null=True)
    pic = models.ImageField(upload_to='goods/', default='')
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    click = models.IntegerField(default=0, null=True)
    unit = models.CharField(max_length=20, null=True)
    isDelete = models.BooleanField(default=False)
    sub_title = models.CharField(max_length=200)
    rest = models.IntegerField(default=100)
    detail = HTMLField(default='')
    type = models.ForeignKey('KindsInfo')