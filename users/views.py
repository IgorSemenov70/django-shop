from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.cache import cache
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from orders.models import OrderItem
from shops.models import Promotion, Offer

from .forms import RegisterForm, BalanceForm
from .service import increase_user_balance


class UserLoginView(LoginView):
    """Представление для аутентификации"""
    template_name = 'users/login.html'


class UserLogoutView(LoginRequiredMixin, LogoutView):
    """Представление для выхода из системы"""
    template_name = 'users/logout.html'


class RegisterView(FormView):
    """Представление для регистрации пользователя"""
    template_name = 'users/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('shops_and_product_list')


def personal_account(request):
    """Представление для просмотра профиля пользователя"""
    username = request.user.username
    promotions_cache_key = 'promotions:{}'.format(username)
    offers_cache_key = 'offers:{}'.format(username)
    promotions = Promotion.objects.all()
    offers = Offer.objects.all()
    user_account_cache_data = {
        promotions_cache_key: promotions,
        offers_cache_key: offers,
    }
    cache.set_many(user_account_cache_data)
    orders_history = OrderItem.objects.filter(user=request.user)
    return render(request, 'users/personal_account.html', context={
        'orders_history': orders_history,
        'promotions': user_account_cache_data[promotions_cache_key],
        'offers': user_account_cache_data[offers_cache_key],
    })


def deposit_balance(request):
    """Представление для пополнения баланса пользователя"""
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            increase_user_balance(user=request.user, balance=form.cleaned_data['balance'])
            return HttpResponseRedirect(reverse_lazy('personal-account'))
    else:
        form = BalanceForm()
    return render(request, 'users/balance.html', {'form': form})
