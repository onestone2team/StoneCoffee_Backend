from mypage.models import Inquiry
from rest_framework import serializers


class InquiryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"