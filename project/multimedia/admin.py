# -*- coding: utf-8 -*-
from django.contrib import admin
from multimedia.models import Foto


class FotoAdmin(admin.TabularInline):
    model = Foto
    search_fields = ('titulo',)


class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'autor', 'fecha_creacion')
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha_creacion',)
    inlines = [
        FotoAdmin,
    ]


