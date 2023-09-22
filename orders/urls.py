from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('cart-items', views.CartItemViewSet, basename='cart-items')

app_name = 'orders'
urlpatterns = router.urls
