from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShopsConfig(AppConfig):
    name = 'shops'
    verbose_name = _('Магазины')
