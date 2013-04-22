# -*- coding: utf-8 -*-
from django.db import models
from utilidades.constantes import ESTADOS
from personal.models import Personal


class Galeria(models.Model):
    codigo = models.AutoField(verbose_name=u'Código', primary_key=True, db_index=True)
    titulo = models.CharField(verbose_name=u'Titulo', max_length=35)
    estado = models.IntegerField(verbose_name=u'Estado', choices=ESTADOS)
    descripcion = models.TextField(verbose_name=u'Acerca de la Galería', max_length=150)
    fecha_creacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Personal, verbose_name=u'Fotografo')
    imagen_portada = models.URLField(verbose_name=u'Imagen Portada')

    class Meta:
        db_table = u'tb_galerias'
        verbose_name = u'Galeria'
        verbose_name_plural = u'Galerias'

    def __unicode__(self):
        return self.titulo


class Foto(models.Model):
    codigo = models.AutoField(verbose_name=u'Código', primary_key=True, db_index=True)
    titulo = models.CharField(verbose_name=u'Titulo', max_length=35)
    descripcion = models.TextField(verbose_name=u'Acerca de la Galería', max_length=150, blank=True, null=True)
    imagen = models.URLField(verbose_name=u'Foto')
    galeria = models.ForeignKey(Galeria, verbose_name=u'Galeria')
    class Meta:
        db_table = u'tb_fotos'
        verbose_name = u'Foto'
        verbose_name_plural = u'Fotos'

    def __unicode__(self):
        return self.titulo


