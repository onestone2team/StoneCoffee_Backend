from rest_framework import serializers
from .models import Survey
from product.models import Product

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ("aroma_grade", "sweet_grade", "acidity_grade", "body_grade")

class ShowProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "product_name", "content", "image")

