from cart.service import Cart
from users.models import User

from .models import Order, OrderItem


def creating_an_order(user: User) -> Order:
    """Создаёт заказ с информацией о пользователе и возвращает созданный объект"""
    obj = Order.objects.create(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone=user.phone,
        city=user.city,
        address=user.address,
        postal_code=user.postal_code,
        paid=True,
    )
    return obj


def creating_an_order_item(user: User, cart: Cart, order: Order) -> None:
    """Создает запись в базе данных о каждом проданном товаре в конкретном заказе"""
    bulk_list = []
    for item in cart:
        bulk_list.append(
            OrderItem(
                user=user,
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'])
        )
    OrderItem.objects.bulk_create(bulk_list)
