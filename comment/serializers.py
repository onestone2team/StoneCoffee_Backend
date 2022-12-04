from rest_framework import serializers
from comment.models import Comment, Nested_Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("image", "comment", "point",)

#지금은 안씀 안쓰면 마지막에 뺄 것
class NestedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nested_Comment
        fields = "__all__"

class NestedCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nested_Comment
        fields = ("nested_comment",)