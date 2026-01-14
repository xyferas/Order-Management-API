from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_amount = serializers.ReadOnlyField()
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Order
        fields = ['id', 'customer', 'items', 'total_amount', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        if not items_data:
            raise serializers.ValidationError("Order must contain at least one item")

        user = self.context['request'].user

        order = Order.objects.create(customer=user)

        for item in items_data:
            product = get_object_or_404(Product, id=item['product_id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price=product.price
            )

        return order

