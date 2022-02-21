from django.contrib import admin

from .models import Shop, Product, Promotion, Offer


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Shop, ShopAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'available', 'created_at', 'updated_at',)
    list_filter = ('available', 'created_at', 'updated_at',)
    list_editable = ('price', 'quantity', 'available',)


admin.site.register(Product, ProductAdmin)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Promotion, PromotionAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Offer, OfferAdmin)
