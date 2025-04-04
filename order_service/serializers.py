# order_service/serializers.py

from rest_framework import serializers
from .models import Order, OrderItem
from item_service.serializers import ItemSerializer
from item_service.models import Item

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_name', 'order_date', 'status', 'total_amount', 'items']
        read_only_fields = ['order_date', 'status', 'total_amount', 'items']
