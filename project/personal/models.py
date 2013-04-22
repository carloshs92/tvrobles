# -*- coding: utf-8 -*-
from django.db import models
from utilidades.constantes import CARGOS, ESTADOS


class Personal(models.Model):
    codigo = models.AutoField(verbose_name=u'Código', primary_key=True, db_index=True)
    nombre = models.CharField(verbose_name=u'Nombres', max_length=25)
    apellido = models.CharField(verbose_name=u'Apellidos', max_length=25)
    descripcion = models.TextField(verbose_name=u'Acerca del Autor', max_length=150)
    website = models.URLField(verbose_name=u'Página Web (opcional)', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    imagen = models.URLField(verbose_name=u'Foto')
    tipo = models.IntegerField(verbose_name=u'Cargo', choices=CARGOS)
    estado = models.IntegerField(verbose_name=u'Estado', choices=ESTADOS)

    class Meta:
        db_table = u'tb_equipo'
        verbose_name = u'Personal'
        verbose_name_plural = u'Personal'

    def __unicode__(self):
        return self.nombre

