from django.db import models
from django.utils.translation import gettext_lazy as _


class Fact(models.Model):
    topic = models.CharField(max_length=20, verbose_name=_('topic'))
    fact = models.TextField(verbose_name=_('fact text'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('creation date'))
    creator = models.CharField(max_length=20, verbose_name=_('creator'))

    def __str__(self):
        return f'{self.topic} - {self.id}'

    class Meta:
        verbose_name = _('Fact')
        verbose_name_plural = _('Facts')
