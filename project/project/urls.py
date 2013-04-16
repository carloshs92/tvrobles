# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from personal.models import Personal
from personal.admin import PersonalAdmin
from multimedia.models import Galeria
from multimedia.admin import GaleriaAdmin
from publicaciones.models import Noticias, Categorias, Revistas
from publicaciones.admin import NoticiasAdmin, RevistasAdmin
from enlaces.models import Asociados
from enlaces.admin import AsociadosAdmin
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
admin.site.register(Revistas, RevistasAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Galeria, GaleriaAdmin)
#admin.site.register(Foto)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Categorias, )
admin.site.register(Asociados, AsociadosAdmin)


urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin-tvrobles/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin-tvrobles/', include(admin.site.urls)),
    (r'^', include('home.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )