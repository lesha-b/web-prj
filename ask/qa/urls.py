from django.conf.urls import url
from qa.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^login/$', test),
    url(r'^signup/$', signup),
    url(r'^question/(?P<id>\d+)/$', show_question),
    url(r'^ask/$', ask),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
]