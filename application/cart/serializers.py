from rest_framework import serializers

from application.cart.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    buyer = serializers.ReadOnlyField(source='customer.email')

    def create(self, validated_data):
        amount = validated_data['amount']
        item = validated_data['item']
        iamount = item.quantity
        if amount > iamount:
            raise serializers.ValidationError(f"not enough product. only {iamount} is available")
        item.quantity -= amount
        item.save()
        return super().create(validated_data)
