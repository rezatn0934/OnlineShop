from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from accounts.authentication import JWTAuthentication
from accounts.permisions import UserIsOwner
from orders.models import CartItem
from orders.serializers import CartItemSerializer


# Create your views here.


class CartItemViewSet(ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated, UserIsOwner)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

