# -*- coding: utf-8 -*-
from django.contrib import admin


class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'autor', 'fecha_creacion')
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha_creacion',)


class FotoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)
    filter_horizontal = ('galeria',)