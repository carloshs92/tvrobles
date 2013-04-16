# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from publicaciones.models import Noticias
from multimedia.models import Galeria, Foto
from enlaces.models import Asociados
from personal.models import Personal
from utilidades.constantes import CARGOS


def get_menu_lateral():
    data = {}
    galerias = Galeria.objects.filter(estado=1).order_by('-fecha_creacion')[:4]
    asociados = Asociados.objects.filter(estado=1).order_by('-pk')[:4]
    data['m_galerias'] = galerias
    data['m_asociados'] = asociados
    return data


def index(request):
    noticias = Noticias.objects.filter(estado=1).order_by('-fecha_creacion')
    portada = Noticias.objects.filter(estado=1, portada=True).order_by('-fecha_creacion')[:3]
    data = get_menu_lateral()
    data['noticias'] = noticias
    data['portadas'] = portada
    return render_to_response(
            'home/index.html', data,
            context_instance=RequestContext(request))


def ver_noticia(request, not_id):
    noticia = get_object_or_404(Noticias, pk=not_id)
    data = get_menu_lateral()
    data['noticia'] = noticia
    return render_to_response(
            'home/noticia.html', data,
            context_instance=RequestContext(request))


def ver_galeria(request, gal_id):
    galeria = get_object_or_404(Galeria, pk=gal_id)
    fotos = Foto.objects.filter(galeria=gal_id, galeria__estado=1)
    data = get_menu_lateral()
    data['fotos'] = fotos
    data['galeria'] = galeria
    return render_to_response(
            'home/galeria.html', data,
            context_instance=RequestContext(request))


def ver_mision(request):
    data = get_menu_lateral()
    return render_to_response(
            'home/mision.html', data,
            context_instance=RequestContext(request))


def ver_nosotros(request):
    data = get_menu_lateral()
    return render_to_response(
            'home/nosotros.html', data,
            context_instance=RequestContext(request))


def contactar(request):
    data = get_menu_lateral()
    return render_to_response(
            'home/nosotros.html', data,
            context_instance=RequestContext(request))


def ver_autores(request):
    data = get_menu_lateral()
    personal = Personal.objects.filter(estado=1)
    lista = list()
    cargos = dict(CARGOS)
    for per in personal:
        dic = {'nombre': per.nombre,
               'apellido': per.apellido,
               'imagen': per.imagen,
               'tipo': cargos[per.tipo],
               'descripcion': per.descripcion}
        lista.append(dic)
    data['personal'] = lista
    return render_to_response(
            'home/autores.html', data,
            context_instance=RequestContext(request))

