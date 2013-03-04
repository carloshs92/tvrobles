# -*- coding: utf-8 -*-
#from django.conf.urls.defaults import patterns, url, include
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('home.views',
    url(r'^$', 'index', name='index'),
    url(r'^noticia/(?P<not_id>\d+)/$', 'ver_noticia', name='ver_noticia')
)