from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

#댓글 조회

    
    
#댓글 추가
class CommentCreateView(APIView):
    def post(self, request):
        pass

#댓글 조회,수정 및 삭제
class CommentDetailView(APIView):
    def get(self, request, product_id, comment_id):
       comment = get_object_or_404(Comment, id=comment_id)
       serializer = CommentSerializer(comment)
       return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request):
        pass
    def delete(self, request):
        pass

#좋아요
class CommentLikeView(APIView):
    def post(self, request):
        pass

#대댓글 추가
class NestedCommentCreatetView(APIView):
    def post(self, request):
        pass


class NestedCommentDetailView(APIView):
    def put(self, request):
        pass
    def delete(self, request):
        pass