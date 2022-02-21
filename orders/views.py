from cart.service import Cart
from django.db import transaction
from django.shortcuts import render, HttpResponse
from users.service import is_there_enough_money, write_off_the_product, change_status, reduce_user_balance

from .service import creating_an_order, creating_an_order_item


def order_created(request):
    """Представление для совершения заказа пользователем"""
    cart = Cart(request)
    if (is_there_enough_money(user=request.user, total_price=cart.get_total_price())
            and write_off_the_product(cart=cart)):
        with transaction.atomic():
            reduce_user_balance(user=request.user, amount=cart.get_total_price())
            change_status(user=request.user)
        obj = creating_an_order(user=request.user)
        creating_an_order_item(user=request.user, cart=cart, order=obj)
        cart.clear()
    else:
        return HttpResponse(
            content='Не удалось выполнить заказ, возможно товар закончился или недостаточно средств,'
                    'проверьте свой баланс и попробуйте повторить заказ.', status=200)
    return render(request, 'orders/order_created.html', {'order': obj})
