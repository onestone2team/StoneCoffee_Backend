from rest_framework import serializers
from .models import Survey
from product.models import Product

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = "__all__"

class ShowProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "name", "content", "image")

