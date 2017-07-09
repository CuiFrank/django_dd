from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/(\d+)/(\d+)/$', views.list),
    url(r'^list/(\d+)/detail/(\d+)/$', views.detail),
]