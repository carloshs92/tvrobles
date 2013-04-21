# -*- coding: utf-8 -*-
from django.forms.util import ErrorList
from django.utils.safestring import mark_safe


class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return u''
        return mark_safe('<h6><div class="alert alert-error">%s</div></h6>' % ''.join([u'<strong>%s</strong>' % e for e in self]))

