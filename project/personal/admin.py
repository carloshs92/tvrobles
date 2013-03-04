# -*- coding: utf-8 -*-
from django.contrib import admin


class PersonalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_creacion', 'tipo')
    search_fields = ('nombre', 'apellido')
    list_filter = ('fecha_creacion', 'tipo')