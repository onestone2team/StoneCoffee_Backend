from rest_framework import serializers
from product.models import Product, Category, Cart
from comment.serializers import ViewCommentSerializer

class ProductSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Product
        fields = "__all__"

class ViewProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "name", "price", "category", "image")

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
    comment_set = ViewCommentSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id","name","content","price","image","like","aroma_grade","sweet_grade","acidity_grade","body_grade","comment_set")
        

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