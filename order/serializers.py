from rest_framework import serializers
from order.models import Order, Payment
from product.models import Product
from product.serializers import ProductNameIdSerializer
class MyOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class UserOrderCreateSerializer(serializers.ModelSerializer):
    product = ProductNameIdSerializer()
    class Meta:
        model = Order
        exclude = ("product_image", "user")
