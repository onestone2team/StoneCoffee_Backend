from mypage.models import Inquiry
from rest_framework import serializers


class InquiryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ("status","title")
        

class AddinquiryListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inquiry
        fields = ("title", "content")