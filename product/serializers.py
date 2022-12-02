from rest_framework import serializers
from product.models import Product, Category



class ProductSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Product
        fields = "__all__"

class ProductCreateSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Product
        fields = "__all__"
    
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class ProductDetailSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    # comments_set = CommentsSerializer(many=True)
    # category = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    def get_category(self, obj):
        return obj.category.category_price

    class Meta:
        model = Product
        fields = "__all__"
        