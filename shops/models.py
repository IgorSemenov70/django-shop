from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    """Модель магазина"""
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Название'))

    class Meta:
        db_table = 'Shop'
        ordering = ('name',)
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_shop', kwargs={'pk': self.pk})


class Product(models.Model):
    """Модель товара"""
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Название товара'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена'))
    quantity = models.PositiveIntegerField(verbose_name=_('Количество'))
    available = models.BooleanField(default=True, verbose_name=_('Наличие'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Дата обновления'))

    class Meta:
        db_table = 'Product'
        ordering = ('name',)
        index_together = ('id',)
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})


class Promotion(models.Model):
    """Модель акций"""
    name = models.CharField(max_length=100, verbose_name=_('Название'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))

    class Meta:
        db_table = 'Promotion'
        ordering = ('name',)
        verbose_name = _('Акция')
        verbose_name_plural = _('Акции')

    def __str__(self):
        return self.name


class Offer(models.Model):
    """Модель предложений"""
    name = models.CharField(max_length=100, verbose_name=_('Название'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))

    class Meta:
        db_table = 'Offer'
        ordering = ('name',)
        verbose_name = _('Предложение')
        verbose_name_plural = _('Предложения')

    def __str__(self):
        return self.name
