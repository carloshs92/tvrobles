# -*- coding: utf-8 -*-
from django.contrib import admin
from project.settings import STATIC_URL


class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'fecha_creacion', 'autor', 'portada')
    search_fields = ('titulo',)
    list_filter = ('autor', 'fecha_creacion')
    filter_horizontal = ('categoria',)

    class Media:
        js = (STATIC_URL + 'js/tinymce/tiny_mce.js',
              STATIC_URL + 'js/editores.js')


class RevistasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'fecha_creacion')
    search_fields = ('titulo',)
    list_filter = ('fecha_creacion', )