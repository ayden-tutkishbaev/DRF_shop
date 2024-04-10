from django.db import models
from django.utils.translation import gettext_lazy as _

from common.utils import validate_phone_number


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    created_at = models.DateTimeField(verbose_name=_('Created_at'),
                                      auto_now_add=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    description = models.TextField(_('Description'))
    discount = models.FloatField(_('Discount'), default=0)
    price = models.FloatField(_('Price'))
    created_at = models.DateTimeField(_('Created_at'), auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.CASCADE)
    short_desc = models.TextField(_('short description'))
    manufacturer = models.ForeignKey('Manufacturer', verbose_name=_('Manufacturer'), on_delete=models.CASCADE)
    view_count = models.IntegerField(_('view count'), default=0)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ForeignKey('common.Media', on_delete=models.CASCADE,
                              verbose_name=_('image'))
    product = models.ForeignKey(Product, verbose_name=_('product'), on_delete=models.CASCADE,
                                related_name='product_images')

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')

    def __str__(self):
        return f'Image Id: {self.id} | Product: {self.product.title}'


class Manufacturer(models.Model):
    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('manufacturer')
        verbose_name_plural = _('manufacturers')

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    title = models.CharField(_('title'), max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'),
                                related_name='characteristics')

    class Meta:
        verbose_name = _('characteristic')
        verbose_name_plural = _('characteristics')

    def __str__(self):
        return self.title


class CharacteristicValue(models.Model):
    title = models.CharField(_('title'), max_length=100)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, verbose_name=_('characteristic'),
                                       related_name='values')

    class Meta:
        verbose_name = _('characteristic value')
        verbose_name_plural = _('characteristic values')

    def __str__(self):
        return self.title


class Instruction(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'))
    left_image = models.ForeignKey('common.Media', verbose_name=_('left image'),
                                   on_delete=models.CASCADE,
                                   related_name='instruction_left_image')
    right_image = models.ForeignKey('common.Media', verbose_name=_('right image'),
                                    on_delete=models.CASCADE,
                                    related_name='instruction_right_image')
    product = models.ForeignKey(Product, verbose_name=_('product'), on_delete=models.CASCADE,
                                related_name='instructions')

    class Meta:
        verbose_name = _('Instruction')
        verbose_name_plural = _('Instructions')

    def __str__(self):
        return self.title


class Order(models.Model):

    class OrderStatus(models.TextChoices):
        NEW = 'new', _('new')
        ACCEPTED = 'accepted', _('accepted')
        PROGRESS = 'progress', _('progress')
        CANCELLED = 'cancelled', _('cancelled')
        FINISHED = 'finished', _('finished')

    full_name = models.CharField(_('full name'), max_length=100)
    phone_number = models.CharField(_('phone number'), max_length=100, validators=[validate_phone_number])
    status = models.CharField(_('status'), max_length=20, choices=OrderStatus.choices, default=OrderStatus.NEW)
    total_price = models.FloatField(_('total price'), default=0)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural= _('orders')

    def __str__(self):
        return self.full_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('order'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('product'), on_delete=models.CASCADE)
    quantity = models.IntegerField(_('quantity'), default=1)

    class Meta:
        verbose_name = _('order item')
        verbose_name_plural = _('order item')
        unique_together = ('order', 'product')

    def __str__(self):
        return f"Id: {self.id} | Q: {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity
