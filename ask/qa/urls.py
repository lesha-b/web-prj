from django.conf.urls import url
from qa.views import *

urlpatterns = [
    url(r'^$', views.test),
    url(r'^login/$', views.test),
    url(r'^singup/$', views.test),
    url(r'^question/(\d+)/$', views.test),
    url(r'^ask/$', views.test),
    url(r'^popular/$', views.test),
    url(r'^new/$', views.test),
]