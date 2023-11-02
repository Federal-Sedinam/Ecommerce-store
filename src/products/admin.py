from django.contrib import admin
from .models import Product, Wishlist, Review, Support, OrderItem, PaymentGateway, Shipping

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(PaymentGateway)
class PaymentGatewayAdmin(admin.ModelAdmin):
    pass

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    pass
