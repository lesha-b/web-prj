from django.conf.urls import url
from qa.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(\d+)/$', show_question),
    url(r'^ask/$', test),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
]