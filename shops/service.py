from typing import List

from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Product, Shop


def best_selling_products() -> List[str]:
    """Возвращает список по наиболее продаваемым товарам за последнюю неделю"""
    products = Product.objects.filter(
        order_items__order__created_at__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
    ).values(
        'name'
    ).annotate(
        max_quantity=Sum('order_items__quantity')
    ).order_by(
        '-max_quantity')[:10]
    return products


def get_current_product(pk: int):
    """Возвращает товар, который есть в наличии"""
    return get_object_or_404(Product, id=pk, available=True)


def get_current_shop(pk: int):
    """Возвращает магазин, если такой существует"""
    return get_object_or_404(Shop, id=pk)


def product_list_by_shop(shop: Shop):
    """Возвращает список товаров продаваемых в конкретном магазине"""
    return Product.objects.filter(shop=shop).only('name')


def products_list_available():
    """Возвращает список товаров в наличии"""
    return Product.objects.filter(available=True).only('name')


def all_shops_list():
    """Возвращает список всех магазинов"""
    return Shop.objects.only('name')
