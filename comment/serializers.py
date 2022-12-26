from rest_framework import serializers
from comment.models import Comment, Nested_Comment
from user.models import UserModel

class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields=('id','profile','profilename',)

class ViewCommentSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer()
    class Meta:
        model = Comment
        fields = ("id", "image", "comment", "point", "user","like","created_at")

class NestedCommentSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer()
    class Meta:
        model = Nested_Comment
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer()
    nested_comment_set = NestedCommentSerializer(many=True)
    class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer()
    class Meta:
        model = Comment
        fields = ("id", "image", "comment", "point", "user",)

class NestedCommentCreateSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer()
    comment_id = serializers.SerializerMethodField

    def get_comment_id(self,obj):
        return obj.comment.id

    class Meta:
        model = Nested_Comment
        fields = ("id", "nested_comment", "comment_id", "user",)

