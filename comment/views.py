from rest_framework.views import APIView
from .models import Comment
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

#댓글 조회
class CommentView(APIView):
    def get(self, request):
       pass
    
#댓글 추가
class CommentCreateView(APIView):
    def post(self, request):
        pass

#댓글 수정 및 삭제
class CommentDetailView(APIView):
    def put(self, request):
        pass
    def delete(self, request):
        pass

#좋아요
class CommentLikeView(APIView):
    def post(self, request):
        pass

#대댓글 추가
class NestedCommenCreatetView(APIView):
    def post(self, request):
        pass


class NestedCommentDetailView(APIView):
    def put(self, request):
        pass
    def delete(self, request):
        pass