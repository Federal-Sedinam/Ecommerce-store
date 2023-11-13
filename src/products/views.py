from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        search = self.request.query_params.get("search", None)

        if search:
            self.queryset = self.queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search),
            )
        return super().get_queryset()


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        search = self.request.query_params.get("search", None)

        if search:
            self.queryset = self.queryset.filter(text__icontains=search)
        return super().get_queryset()


class SupportListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = models.Support.objects.all()
        search = request.query_params.get("search", None)
        if search:
            queryset = queryset.filter(
                Q(subject__icontains=search) | Q(message__icontains=search),
            )
        serializer = serializers.SupportSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.SupportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SupportDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.Support, id=pk)
        serializer = serializers.SupportSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.Support, id=pk)
        serializer = serializers.SupportSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.Support, id=pk)
        serializer = serializers.SupportSerializer(
            instance,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(models.Support, id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemListView(APIView):
    def get(self, request, *args, **kwargs):
        orderitem = models.OrderItem.objects.all()
        serializer = serializers.OrderItemSerializer(orderitem, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.OrderItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderItemDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.OrderItem, id=pk)
        serializer = serializers.OrderItemSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.OrderItem, id=pk)
        serializer = serializers.OrderItemSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.OrderItem, id=pk)
        serializer = serializers.OrderItemSerializer(
            instance,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(models.OrderItem, id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentGatewayListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = models.PaymentGateway.objects.all()
        search = request.query_params.get("search", None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        serializer = serializers.PaymentGatewaySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.PaymentGatewaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PaymentGatewayDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.PaymentGateway, id=pk)
        serializer = serializers.PaymentGatewaySerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.PaymentGateway, id=pk)
        serializer = serializers.PaymentGatewaySerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.PaymentGateway, id=pk)
        serializer = serializers.PaymentGatewaySerializer(
            instance,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(models.PaymentGateway, id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShippingListView(APIView):
    def get(self, request, *args, **kwargs):
        shipping = models.Shipping.objects.all()
        serializer = serializers.ShippingSerializer(shipping, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.ShippingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShippingDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.Shipping, id=pk)
        serializer = serializers.ShippingSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.Shipping, id=pk)
        serializer = serializers.ShippingSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(models.Shipping, id=pk)
        serializer = serializers.ShippingSerializer(
            instance,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(models.Shipping, id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.Promotionserializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.Cartserializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     total_price = sum(item.products.price * item.quantity for item in queryset)
    #     response_data = {
    #         "cart_items": serializer.data,
    #         "total_price": total_price
    #     }
        
    #     return Response(response_data)
    