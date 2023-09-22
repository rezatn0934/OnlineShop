from rest_framework import serializers

from .models import Cart, CartItem, Product


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
