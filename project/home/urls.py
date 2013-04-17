# -*- coding: utf-8 -*-
#from django.conf.urls.defaults import patterns, url, include
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('home.views',
    url(r'^$', 'index', name='index'),
    url(r'^noticia/(?P<not_id>\d+)/$', 'ver_noticia', name='ver_noticia'),
    url(r'^galeria/(?P<gal_id>\d+)/$', 'ver_galeria', name='ver_galeria'),
    url(r'^mision-y-vision/$', 'ver_mision', name='ver_mision'),
    url(r'^nosotros/$', 'ver_nosotros', name='ver_nosotros'),
    url(r'^integrantes/$', 'ver_autores', name='ver_autores'),
    url(r'^contactenos/$', 'contactar', name='contactar'),
    url(r'^revista-online/(?P<rev_id>\d+)/$', 'ver_revista', name='ver_revista'),
    url(r'^calendario/$', 'ver_calendario', name='ver_calendario')
)