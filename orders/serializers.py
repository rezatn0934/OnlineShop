from rest_framework import serializers

from .models import Cart, CartItem, Product


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def validate(self, attrs):
        product = Product.objects.filter(pk=attrs['product'])
        quantity = attrs['quantity']
        if product.quantity < quantity:
            raise serializers.ValidationError('Product quantity is less than what you want!')
        return attrs
