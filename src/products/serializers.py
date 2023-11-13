from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    new_price =serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Product
        fields = "__all__"
    def get_new_price(self, instance):
        promotions = instance.promotions.all()

        new_price = float(instance.price)
        for promotion in promotions:
            new_price = new_price - new_price * (float(promotion.percentage_discount) / 100)
        return f"{new_price:.2f}"


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wishlist
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Support
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = "__all__"


class PaymentGatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentGateway
        fields = "__all__"


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shipping
        fields = "__all__"


class Promotionserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Promotion
        fields = "__all__"


class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = "__all__"
        
    def to_representation(self, instance): 
        representation =  super().to_representation(instance)
        representation["total_price"] = sum([models.Product.objects.get(pk=product_id).price for product_id in representation.get("products")])
        return representation
