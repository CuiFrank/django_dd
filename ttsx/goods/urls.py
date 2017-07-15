from django.conf.urls import include, url


from .views import *
from .search_view import *

urlpatterns = [
    url(r'^$', index),
    url(r'^list/(\d+)/(\d+)/(\d+)/$', list),
    url(r'^list/(\d+)/detail/(\d+)/$', detail),


    url(r'^search/?$', MySearchView.as_view()),

]