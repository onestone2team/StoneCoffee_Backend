from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


#댓글 추가
class CommentCreateView(APIView):
    def post(self, request, product_id):
        serializer = CommentCreateSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # serializer.save(user=request.user) #이게 원래꺼 에러나서 빼뚬
            return Response({"data":serializer.data,"message":"댓글 등록 완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors":serializer.errors,"message":"댓글 등록 실패"}, status=status.HTTP_400_BAD_REQUEST)


#댓글 및 대댓글 조회,수정 및 삭제
class CommentDetailView(APIView):
    def get(self, request, product_id, comment_id):
       comment = get_object_or_404(Comment, id=comment_id)
       serializer = CommentSerializer(comment)
       return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, product_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)# 이게 또 들어가는게 맞나 request.data에 다 들어가는게 아닌가??? 12/3)
        serializer = CommentCreateSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "해당 글이 수정되었습니다.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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