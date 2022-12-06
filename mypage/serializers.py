from rest_framework import serializers
from order.models import Order, Payment


class MyPaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


