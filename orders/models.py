from django.db import models
from django.utils.translation import gettext_lazy as _
from shops.models import Product
from users.models import User


class Order(models.Model):
    """Модель заказа"""
    first_name = models.CharField(max_length=50, verbose_name=_('Имя'))
    last_name = models.CharField(max_length=50, verbose_name=_('Фамилия'))
    email = models.EmailField(verbose_name=_('Электронная почта'))
    address = models.CharField(max_length=250, null=True, blank=True, verbose_name=_('Адрес'))
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Телефон'))
    postal_code = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Индекс'))
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Город'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Дата оплаты'))
    paid = models.BooleanField(default=False, verbose_name=_('Оплачено'))

    class Meta:
        db_table = 'Order'
        ordering = ('-created_at',)
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_cost(self):
        """Возвращает общую стоимость заказа"""
        return sum(item.get_cost() for item in self.objects.all())


class OrderItem(models.Model):
    """Модель проданного товара из конкретного заказа"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Количество'))

    class Meta:
        db_table = 'OrderItem'
        verbose_name = _('Информация о заказе')
        verbose_name_plural = _('Информация о заказах')

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        """Возвращает общую стоимость товара с учётом количества"""
        return self.price * self.quantity
