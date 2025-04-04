# payment_service/serializers.py

from rest_framework import serializers
from .models import Payment
from order_service.models import Order

class PaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(),
        source='order',
        write_only=True
    )

    class Meta:
        model = Payment
        fields = ['id', 'order_id', 'method', 'status', 'transaction_id', 'created_at']
        read_only_fields = ['id', 'status', 'transaction_id', 'created_at']
