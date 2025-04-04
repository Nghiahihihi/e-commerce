# item_service/serializers.py

from rest_framework import serializers
from .models import Item, Provider

# Serializer cho Provider
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

# Serializer cho Item
class ItemSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer()

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        provider_data = validated_data.pop('provider')
        provider, created = Provider.objects.get_or_create(**provider_data)
        item = Item.objects.create(provider=provider, **validated_data)
        return item

    def update(self, instance, validated_data):
        provider_data = validated_data.pop('provider', None)
        
        # Update provider info
        if provider_data:
            provider = instance.provider
            for attr, value in provider_data.items():
                setattr(provider, attr, value)
            provider.save()

        # Update item fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance