from django.urls import path

from . import views

urlpatterns = [
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add_cart/<int:pk>/', views.cart_add, name='cart_add'),
    path('remove_cart/<int:pk>/', views.cart_remove, name='cart_remove'),
]
