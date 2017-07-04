from django.conf.urls import include, url

from . import views

urlpatterns = [

    url(r'^list/$', views.list),
    url(r'^detail/$', views.detail),
]