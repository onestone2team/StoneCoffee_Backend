from rest_framework import serializers
from product.models import Product, Category, Cart



class ProductSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Product
        fields = "__all__"

class ProductCreateSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(
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
        
class ProductDetailViewSerializer(serializers.ModelSerializer):
    Catagory_id = serializers.SerializerMethodField()

    def get_Catagory_id(self, obj):
        return obj.Catagory_id.type

    class Meta:
        model = Product
        fields = ("id","product_name","price","image","Catagory_id")

class CartSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("product","count", "price","weight","product_image")

class CartViewSerializer(serializers.ModelSerializer):
    product = ProductDetailViewSerializer()

    class Meta:
        model = Cart
        fields = ("id","product", "weight", "count")

class ProductNameIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name")