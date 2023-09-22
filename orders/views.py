from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from accounts.authentication import JWTAuthentication
from accounts.permisions import UserIsOwner
from orders.models import CartItem, Cart, Order, OrderItem
from orders.serializers import CartItemSerializer
from store.models import Product


# Create your views here.


class CartItemViewSet(ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated, UserIsOwner)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CheckOutView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated, UserIsOwner)

    def post(self):
        user = self.request.user
        cart = Cart.objects.filter(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        order = Order.objects.create(customer=user)
        order_details = []
        for cart_item in cart_items:
            order_details.append(OrderItem(order=order, product=cart_item.product, quantity=cart_item.quantity,
                                             unit_price=cart_item.product.price))
            product = Product.objects.get(pk=cart_item.product.id)
            product.quantity -= cart_item.quantity
            product.save()

        OrderItem.objects.bulc_create(order_details)
        Cart.objects.delete()
