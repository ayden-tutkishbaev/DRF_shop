import datetime
from mptt.models import MPTTModel, TreeForeignKey
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.db import models


class ServiceCategory(MPTTModel):
    title = models.CharField(_('Title'), max_length=100)
    order = models.IntegerField(_('order'), default=0)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        self.title

    class Meta:
        verbose_name = _('Service category')
        verbose_name_plural = _('Service categories')

    class MPTTMeta:
        order_insertion_by = ['title']


class Service(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    subtitle = models.CharField(_('Subtitle'), max_length=100)
    image = models.ForeignKey('common.Media', on_delete=models.CASCADE, verbose_name=_('Image'))
    purpose = models.CharField(_('Purpose'), max_length=100)
    short_description = models.TextField(_('Short Description'))
    description = models.TextField(_('Description'))
    price = models.IntegerField(_('Price'))
    category = models.ForeignKey(ServiceCategory, verbose_name=_('Category'), related_name='services', on_delete=models.CASCADE)
    is_home_page = models.BooleanField(_('is home page'), default=False, unique=True)
    gif = models.ForeignKey('common.Media', on_delete=models.CASCADE, verbose_name=_('gif'), related_name='service_gif')

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.title


class ImageService(models.Model):
    image = models.ForeignKey('common.Media', on_delete=models.CASCADE, verbose_name=_('Image'))
    service = models.ForeignKey('common.Media', on_delete=models.CASCADE, verbose_name=_('Service'), related_name='images')

    class Meta:
        verbose_name = _('Service image')
        verbose_name_plural = _('Service images')

    def __str__(self):
        return f'Id: {self.id}|Service: {self.service.title}'


class Characteristics(models.Model):
    title = models.CharField(_('title'), max_length=100)
    value = models.CharField(_('value'), max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_('service'), related_name='characteristics')

    class Meta:
        verbose_name = _('characteristic')
        verbose_name_plural = _('characteristics')

    def __str__(self):
        return self.title


class ProcedureCost(models.Model):
    title = models.CharField(_('title'), max_length=100)
    price = models.CharField(_('price'), max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_('service'), related_name='procedure_cost')

    class Meta:
        verbose_name = _('procedure cost')
        verbose_name_plural = _('procedure costs')


