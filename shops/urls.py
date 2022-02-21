from django.urls import path

from . import views
from .views import PromotionCreateView, OfferCreateView, ProductCreateView, CreateShopView

urlpatterns = [
    path('main_page/', views.product_list, name='shops_and_product_list'),
    path('main_page/<int:pk>/', views.product_list, name='product_list_by_shop'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('promotion/', PromotionCreateView.as_view(), name='create_promotion'),
    path('offer/', OfferCreateView.as_view(), name='create_offer'),
    path('product/', ProductCreateView.as_view(), name='create_product'),
    path('create_shop/', CreateShopView.as_view(), name='create_shop'),
    path('product_statistics/', views.product_statistics, name='product_statistics')
]
