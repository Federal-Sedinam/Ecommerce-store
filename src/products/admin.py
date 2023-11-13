from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Support)
class SupportAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PaymentGateway)
class PaymentGatewayAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Shipping)
class ShippingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    pass
