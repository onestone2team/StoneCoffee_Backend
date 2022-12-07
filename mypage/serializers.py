from rest_framework import serializers
from order.models import Payment


class MyPaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


