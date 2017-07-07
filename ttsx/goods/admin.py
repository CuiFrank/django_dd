from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import *


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']


class KindsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'kinds']



admin.site.register(GoodsInfo, GoodsInfoAdmin)
admin.site.register(KindsInfo, KindsInfoAdmin)