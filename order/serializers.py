from rest_framework import serializers
from order.models import Order, Payment

class MyOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class UserOrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

class PaymentSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("created_at","total_price","user")