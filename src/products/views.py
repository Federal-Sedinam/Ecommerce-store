from rest_framework import viewsets
from .models import Product, Wishlist, Review,  Support, OrderItem, PaymentGateway, Shipping
from .serializers import ProductSerializer, WishlistSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@permission_classes([AllowAny])
class SupportView(APIView):
    def post(self, request, *args, **kwargs):
        instance = Support.objects.create(**request.data)
        return Response(instance, status=status.HTTP_201_CREATED)

class OrderItemView(APIView):
    pass


class PaymentGatewayView(APIView):
    pass

class ShippingView(APIView):
    pass

    
# class SupportViewSet(viewsets.ModelViewSet):
#     queryset = Support.objects.all()
#     serializer_class = SupportSerializer

# class OrderItemViewSet(viewsets.ModelViewSet):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer

# class PaymentGatewayViewSet(viewsets.ModelViewSet):
#     queryset = PaymentGateway.objects.all()
#     serializer_class = PaymentGatewaySerializer

# class ShippingViewSet(viewsets.ModelViewSet):
#     queryset = Shipping.objects.all()
#     serializer_class = ShippingSerializer
