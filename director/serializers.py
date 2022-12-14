from mypage.models import Inquiry
from order.models import Order
from rest_framework import serializers
from order.models import Payment

class AdminProductView(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self,obj):
        return obj.user.profilename

    class Meta:
        model = Order
        fields = "__all__"

class AdminProductStatusEdit(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id","status",)

class AddadminInquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry
        fields = ("answer", "status")

class AdminInquiryListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self,obj):
        return obj.user.profilename
    class Meta:
        model = Inquiry
        fields = ("id","status","title","created_at","content","answer","user")