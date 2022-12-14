from mypage.models import Inquiry
from rest_framework import serializers
from order.models import Payment

class InquiryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ("id","status","title","created_at","content","answer","category")

class AddinquiryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry
        fields = ("title", "content", "category")

class InquiryDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    def get_user(self,obj):
        return obj.user.profilename

    def get_product(self,obj):
        return obj.product.product_name

    class Meta:
        model = Inquiry
        fields = ("user", "title", "content","status", "answer", "category", "created_at", "updated_at", "product")

class MyPaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"



