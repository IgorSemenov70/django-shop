from .service import Cart


def cart(request):
    """Метод для отображения состояния корзины"""
    return {'cart': Cart(request)}
