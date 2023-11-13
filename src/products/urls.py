from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"wishlist", views.WishlistViewSet, basename="wishlist")
router.register(r"review", views.ReviewViewSet, basename="review")
router.register(r"promotion", views.PromotionViewSet, basename="promotion")
router.register(r"cart", views.CartViewSet, basename="cart")

urlpatterns = router.urls

urlpatterns += [
    path("support/<int:pk>/", views.SupportDetailView.as_view()),
    path("support/", views.SupportListView.as_view()),
    path("orderItem/<int:pk>/", views.OrderItemDetailView.as_view()),
    path("orderItem/", views.OrderItemListView.as_view()),
    path("paymentGateway/<int:pk>/", views.PaymentGatewayDetailView.as_view()),
    path("paymentGateway/", views.PaymentGatewayListView.as_view()),
    path("shipping/<int:pk>/", views.ShippingDetailView.as_view()),
    path("shipping/", views.ShippingListView.as_view()),
]
