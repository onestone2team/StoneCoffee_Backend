from mypage.models import Inquiry
from rest_framework import serializers
from order.models import Payment

class InquiryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ("status","title")


class AddinquiryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry
        fields = ("title", "content")


class AddadminInquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry
        fields = ("answer", "status")

class MyPaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"



