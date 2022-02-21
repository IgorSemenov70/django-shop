from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Модель пользователя"""
    phone = models.CharField(max_length=30, blank=True, verbose_name=_('Телефон'))
    email = models.EmailField(verbose_name=_('Электронная почта'))
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Город'))
    address = models.CharField(max_length=250, null=True, blank=True, verbose_name=_('Адрес'))
    postal_code = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Индекс'))
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=_('баланс'))
    status = models.CharField(max_length=30, default='Новичок', verbose_name=_('Статус'))
    purchase_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=_('Сумма покупок'))

    class Meta(AbstractUser.Meta):
        db_table = 'Users'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
