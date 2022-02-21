from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class AuthForm(forms.Form):
    """Форма для аутентификации"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    """Форма для регистрации"""
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'phone', 'city', 'address',
                  'postal_code')


class BalanceForm(forms.Form):
    """Форма для пополнения баланса"""
    balance = forms.DecimalField(max_digits=10, decimal_places=2)
