from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^register_name/$', views.register_name),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login_handle/$', views.login_handle),
    url(r'^logout/$', views.logout),
    url(r'^myemail/$', views.my_email),

]