from rest_framework import serializers
from .models import Price

class PriceSerializer(serializers.Serializer):
    date = serializers.CharField(max_length=30)
    open_price = serializers.CharField(max_length=30)
    close_price = serializers.CharField(max_length=30)

    def create(self, validate_data):
        return Price.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.open_price = validated_data.get('open_price', instance.open_price)
        instance.close_price = validated_data.get('close_price', instance.close_price)
        instance.save()
        return instance