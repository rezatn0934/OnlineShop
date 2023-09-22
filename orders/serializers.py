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

    def create(self, validated_data):
        cart = Cart.objects.get_or_create(user=self.context['request'].user)
        return CartItem.objects.create(cart=cart, **validated_data)
