# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from publicaciones.models import Noticias
from enlaces.models import Asociados


def index(request):
    noticias = Noticias.objects.filter(estado=1).order_by('-fecha_creacion')
    portada = Noticias.objects.filter(estado=1, portada=True).order_by('-fecha_creacion')[:3]
    asociados = Asociados.objects.filter(estado=1)
    return render_to_response(
            'home/index.html', {'noticias': noticias, 'portadas': portada, 'asociados': asociados},
            context_instance=RequestContext(request))


def ver_noticia(request, not_id):
    noticia = get_object_or_404(Noticias, pk=not_id)
    asociados = Asociados.objects.filter(estado=1)
    return render_to_response(
            'home/noticia.html', {'noticia': noticia, 'asociados': asociados},
            context_instance=RequestContext(request))