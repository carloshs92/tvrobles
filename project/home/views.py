# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from publicaciones.models import Noticias, Revistas
from multimedia.models import Galeria, Foto
from enlaces.models import Asociados
from personal.models import Personal
from utilidades.constantes import CARGOS
from home.forms import ContactForm
from utilidades.scripts import DivErrorList
from django.contrib import messages


def get_menu_lateral():
    data = {}
    galerias = Galeria.objects.filter(estado=1).order_by('-fecha_creacion')[:4]
    asociados = Asociados.objects.filter(estado=1).order_by('-pk')[:4]
    try:
        revistas = Revistas.objects.filter(estado=1).order_by('-pk')[0]
    except:
        revistas = None
    data['m_galerias'] = galerias
    data['m_asociados'] = asociados
    data['m_revistas'] = revistas
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


def ver_noticia(request, not_id, url_amigable):
    noticia = get_object_or_404(Noticias, pk=not_id)
    data = get_menu_lateral()
    data['noticia'] = noticia
    return render_to_response(
            'home/noticia.html', data,
            context_instance=RequestContext(request))


def ver_galeria(request, gal_id, url_amigable):
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
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            mensaje_envio = request.POST['contenido'] == '' and request.POST['web'] or request.POST['contenido'] + '- Pagina web: %s' % request.POST['web']
            recipients = ['carlos.hs.92@gmail.com']

            from django.core.mail import send_mail
            send_mail('contactenos - %s' % request.POST['nombres'],
                      mensaje_envio + ' - Correo: ' + request.POST['correo'],
                      'portalineiperu@gmail.com', recipients)

            form.cleaned_data['nombres']
            form.cleaned_data['correo']
            form.cleaned_data['web']
            form.cleaned_data['contenido']
            messages.add_message(request, messages.SUCCESS, "Su mensaje ha sido enviado")

    else:
        form = ContactForm(error_class=DivErrorList)
    data = get_menu_lateral()
    data['form'] = form
    return render_to_response(
            'home/contactenos.html', data,
            context_instance=RequestContext(request))


def ver_revista(request, rev_id, url_amigable):
    revista = get_object_or_404(Revistas, pk=rev_id)
    data = get_menu_lateral()
    data['revista'] = revista
    return render_to_response(
            'home/revista_online.html', data,
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


def ver_calendario(request):
    data = get_menu_lateral()
    return render_to_response(
            'home/calendario.html', data,
            context_instance=RequestContext(request))

