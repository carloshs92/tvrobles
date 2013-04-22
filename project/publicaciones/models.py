# -*- coding: utf-8 -*-
from django.db import models
from utilidades.constantes import ESTADOS
from personal.models import Personal
from multimedia.models import Galeria


class Categorias(models.Model):
    codigo = models.AutoField(verbose_name=u'Código', primary_key=True, db_index=True)
    titulo = models.CharField(verbose_name=u'Categoria', max_length=45)

    class Meta:
        db_table = u'tb_categorias'
        verbose_name = u'Categoría'
        verbose_name_plural = u'Categorías'

    def __unicode__(self):
        return self.titulo


class Noticias(models.Model):
    codigo = models.AutoField(verbose_name=u'Código', primary_key=True, db_index=True)
    titulo = models.CharField(verbose_name=u'Titulo', max_length=45)
    estado = models.IntegerField(verbose_name=u'Estado', choices=ESTADOS)
    portada = models.BooleanField(verbose_name=u'Colocar en el Banner Principal')
    contenido = models.TextField(verbose_name=u'Contenido')
    fecha_creacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Personal, verbose_name=u'Autor')
    imagen_principal = models.URLField(verbose_name=u'Imagen - Banner (opcional)', blank=True, null=True)
    imagen_reporte = models.URLField(verbose_name=u'Imagen - Reporte')
    video = models.URLField(verbose_name=u'Video (opcional)', blank=True, null=True)
    galeria = models.ForeignKey(Galeria, verbose_name=u'Galeria (opcional)', blank=True, null=True,)
    categoria = models.ManyToManyField(Categorias, verbose_name=u'Categoría')

    class Meta:
        db_table = u'tb_noticia'
        verbose_name = u'Noticia'
        verbose_name_plural = u'Noticias'

    def __unicode__(self):
        return self.titulo


#http://es.calameo.com/
#http://issuu.com/
class Revistas(models.Model):
    codigo = models.AutoField(verbose_name=u'Código', primary_key=True, db_index=True)
    titulo = models.CharField(verbose_name=u'Titulo', max_length=55)
    estado = models.IntegerField(verbose_name=u'Estado', choices=ESTADOS)
    fecha_creacion = models.DateTimeField(auto_now=True)
    contenido = models.TextField(verbose_name=u'Contenido')
    imagen_principal = models.URLField(verbose_name=u'Imagen - Portada (opcional)', blank=True, null=True)

    class Meta:
        db_table = u"tb_revistas"
        verbose_name = u'Revista'
        verbose_name_plural = u'Revistas'

    def __unicode__(self):
        return self.titulo