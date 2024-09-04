from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=5, decimal_places=2)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    category = models.SmallIntegerField(
        verbose_name=_('Category'),
        choices=((1, 'category_1'), (2, 'category_2'), (3, 'category_3'), (4, 'category_4')))
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    create = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    def __str__(self):
        return f"Product name {self.title} - Price {self.price}"

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['-id']
