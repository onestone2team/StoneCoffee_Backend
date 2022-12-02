from rest_framework import serializers
from comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    product_id = serializers.SerializerMethodField()
    
    def get_user_id(self,obj):
        return obj.user.id
    def get_product_id(self,obj):
        return obj.product.id
    
    class Meta:
        model = Comment
        fields = "__all__"
