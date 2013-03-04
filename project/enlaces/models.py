# -*- coding: utf-8 -*-
from django.db import models
from utilidades.constantes import ESTADOS


class Asociados(models.Model):
    codigo = models.AutoField(verbose_name=u'Código', primary_key=True, db_index=True)
    nombre = models.CharField(verbose_name=u'Nombre', max_length=45)
    estado = models.IntegerField(verbose_name=u'Estado', choices=ESTADOS)
    importante = models.BooleanField(verbose_name=u'Colocar tambien dentro del pie de página')
    logo = models.CharField(verbose_name=u'Logo', max_length=200, blank=True, null=True)
    url = models.CharField(verbose_name=u'URL', max_length=200, blank=True, null=True)

    class Meta:
        db_table = u"tb_asociados"
        verbose_name = u'Asociado'
        verbose_name_plural = u'Asociados'

    def __unicode__(self):
        return self.nombre


