from cart.forms import CartAddProductForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Shop, Product, Promotion, Offer
from .service import best_selling_products, get_current_product, get_current_shop, product_list_by_shop, \
    products_list_available, all_shops_list


class CreateShopView(CreateView):
    """Представление для создания магазина"""
    model = Shop
    template_name = 'shops/create_shop.html'
    fields = '__all__'
    success_url = reverse_lazy('shops_and_product_list')


class ProductCreateView(CreateView):
    """Представление для создания товара"""
    model = Product
    template_name = 'shops/create_product.html'
    fields = ('shop', 'name', 'description', 'price', 'quantity',)
    success_url = reverse_lazy('shops_and_product_list')


class PromotionCreateView(CreateView):
    """Представление для создания акции"""
    model = Promotion
    template_name = 'shops/create_promotion.html'
    fields = '__all__'
    success_url = reverse_lazy('personal-account')


class OfferCreateView(CreateView):
    """Представление для создания предложения"""
    model = Offer
    template_name = 'shops/create_offer.html'
    fields = '__all__'
    success_url = reverse_lazy('personal-account')


def product_list(request, pk=None):
    """Представление для отображения товаров"""
    shop = None
    shops = all_shops_list()
    products = products_list_available()
    if pk:
        shop = get_current_shop(pk=pk)
        products = product_list_by_shop(shop=shop)
    return render(request, 'shops/shops_and_product_list.html', {'shop': shop, 'shops': shops, 'products': products})


def product_detail(request, pk):
    """Представление для детального просмотра товара"""
    product = get_current_product(pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request, 'shops/product_detail.html', {'product': product, 'cart_product_form': cart_product_form})


def product_statistics(request):
    """Представление для отображения статистики по продажам товаров"""
    products = best_selling_products()
    return render(request, 'shops/product_statistics.html', {'products': products})
