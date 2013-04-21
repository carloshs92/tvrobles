# -*- coding: utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    nombres = forms.CharField(max_length=100, label='Nombres')
    correo = forms.EmailField(max_length=100, label='Correo')
    web = forms.URLField(max_length=100, required=False, label='Web')
    contenido = forms.CharField(max_length=100, widget=forms.Textarea, label='Contenido')
