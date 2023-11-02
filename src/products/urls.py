from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, WishlistViewSet, ReviewViewSet
from . import views

# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')
# router.register(r'wishlist', WishlistViewSet, basename='wishlist')
# router.register(r'review', ReviewViewSet, basename='review')

# urlpatterns = router.urls

urlpatterns = [
    path('support/', views.SupportView, name='support'),
    path('orderItem/', views.OrderItemView, name='OrderItem'),
    path('payment/', views.PaymentGateway, name='Paymentgateway'),
    path('shipping/', views.Shipping, name='Shipping'),
]

# router.register(r'support', SupportViewSet,basename='support')
# router.register(r'orderItem', OrderItemViewSet, basename='orderitem')
# router.register(r'paymentGateway', PaymentGatewayViewSet, basename='payment')
# router.register(r'shipping', ShippingViewSet, basename='shipping')
