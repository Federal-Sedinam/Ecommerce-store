from .models import Product, Wishlist, Review
# Support, OrderItem, PaymentGateway, Shipping
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# class SupportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Support
#         fields = '__all__'

# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = '__all__'

# class PaymentGatewaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PaymentGateway
#         fields = '__all__'

# class ShippingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shipping
#         fields = '__all__'
        