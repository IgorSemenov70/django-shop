from django import forms

from .models import Shop, Product, Promotion, Offer


class ShopForm(forms.ModelForm):
    """Форма для добавления магазина"""

    class Meta:
        model = Shop


class ProductForm(forms.ModelForm):
    """Форма для добавления товара"""

    class Meta:
        model = Product


class PromotionForm(forms.ModelForm):
    """Форма для добавления акции"""

    class Meta:
        model = Promotion


class OfferForm(forms.ModelForm):
    """Форма для добавления предложения"""

    class Meta:
        model = Offer
