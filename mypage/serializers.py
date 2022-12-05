from rest_framework import serializers
from order.models import Order


class MyPaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class PaymentSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
