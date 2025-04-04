# cart_service/serializers.py

from rest_framework import serializers
from .models import Cart, CartItem
from item_service.models import Item
from item_service.serializers import ItemSerializer

class CartItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(), source='item', write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'item_id', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items']
        read_only_fields = ['customer']
