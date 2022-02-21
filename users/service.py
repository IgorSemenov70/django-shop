from cart.service import Cart
from shops.models import Product

from .models import User


def write_off_the_product(cart: Cart) -> bool:
    """Проверяет наличие каждой единицы товара на складе, которая находится в корзине"""
    if all([_product_in_stock(item=item) for item in cart]):
        return True


def is_there_enough_money(user: User, total_price: float) -> bool:
    """Проверяет достаточно ли средств на балансе у пользователя для совершения заказа"""
    if user.balance >= total_price:
        return True


def increase_user_balance(user: User, balance: float) -> None:
    """Метод увеличивающий баланс пользователя"""
    user.balance += balance
    user.save(update_fields=['balance'])


def change_status(user: User) -> None:
    """Метод изменяющий баланс пользователя в зависимости от общей суммы покупок"""
    if user.purchase_amount >= 10000:
        user.status = 'Продвинутый'
    elif user.purchase_amount >= 100000:
        user.status = 'Эксперт'
    user.save(update_fields=['status'])


def reduce_user_balance(user: User, amount: float) -> None:
    """Метод уменьшающий баланс пользователя"""
    user.balance -= amount
    user.purchase_amount += amount
    user.save(update_fields=['balance', 'purchase_amount'])


def _product_in_stock(item: Product) -> bool:
    """Проверяет наличие товара на складе для совершения заказа пользователем"""
    product = Product.objects.get(id=item['product'].id)
    if product.quantity >= item['quantity']:
        product.quantity -= item['quantity']
        product.save(update_fields=['quantity'])
        return True
    elif product.quantity == 0:
        product.available = False
        product.save(update_fields=['available'])
