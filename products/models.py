from django.db import models
from django.utils.translation import gettext_lazy as _

from common.utils import validate_phone_number


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    description = models.TextField(_('Description'))
    discount = models.FloatField(_('discount'), default=0)
    price = models.FloatField(_('Price'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    short_description = models.TextField(_('Short description'))
    manufacturer = models.ForeignKey("Manufacturer", verbose_name=_('Manufacturer'), on_delete=models.CASCADE)
    view_count = models.IntegerField(_('View count'), default=0)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title



