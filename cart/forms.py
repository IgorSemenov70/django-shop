from django import forms


class CartAddProductForm(forms.Form):
    """Форма для добавления товара в корзину"""
    quantity = forms.IntegerField(min_value=0)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
