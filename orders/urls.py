from django.urls import path

from . import views

urlpatterns = [
    path('create_order/', views.order_created, name='order_created'),
]
