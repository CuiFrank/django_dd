from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cart/$', views.cart),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^place_order/$', views.place_order),
]
