# customer_service/serializers.py

from rest_framework import serializers
from .models import Customer, Address

# Serializer for Address
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

# Serializer for Customer with nested Address
class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        customer = Customer.objects.create(address=address, **validated_data)
        return customer
