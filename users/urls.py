from django.urls import path

from . import views
from .views import UserLoginView, UserLogoutView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('balance/', views.deposit_balance, name='balance'),
    path('personal_account/', views.personal_account, name='personal-account'),
]
