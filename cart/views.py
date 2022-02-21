from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shops.models import Product

from .forms import CartAddProductForm
from .service import Cart


@require_POST
def cart_add(request, pk):
    """Представление для добавления товара в корзину"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, pk):
    """Представление для удаления товара из корзины"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    """Представление для отображения корзины"""
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart_detail.html', {'cart': cart})
