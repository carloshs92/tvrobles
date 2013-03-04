# -*- coding: utf-8 -*-
from django.contrib import admin


class AsociadosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'importante')
    search_fields = ('nombre',)