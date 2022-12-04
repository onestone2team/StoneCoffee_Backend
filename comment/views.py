from rest_framework.views import APIView
from .models import Comment, Nested_Comment
from .serializers import CommentSerializer, CommentCreateSerializer, NestedCommentSerializer, NestedCommentCreateSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


#댓글 추가
class CommentCreateView(APIView):
    def post(self, request, product_id):
        serializer = CommentCreateSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(product_id=product_id, user=request.user)
            return Response({"data":serializer.data,"message":"댓글 등록 완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors":serializer.errors,"message":"댓글 등록 실패"}, status=status.HTTP_400_BAD_REQUEST)


#댓글 및 대댓글 조회, 댓글 수정 및 삭제
class CommentDetailView(APIView):
    def get(self, request, product_id, comment_id):
       comment = get_object_or_404(Comment, id=comment_id)
       serializer = CommentSerializer(comment)
       return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, product_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentCreateSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "해당 댓글이 수정되었습니다.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, product_id, comment_id):
        comment = Comment.objects.filter(Q(user_id=request.user.id)&Q(product_id=product_id)&Q(id=comment_id))
        comment.delete()
        return Response({"message": "해당 댓글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

#좋아요
class CommentLikeView(APIView):
    def post(self, request, product_id, comment_id):
        comment_list = get_object_or_404(Comment, id=comment_id, product_id= product_id)
        if request.user in comment_list.like.all():
            comment_list.like.remove(request.user)
            return Response({"message":"좋아요를 취소했습니다"}, status=status.HTTP_200_OK)
        else:
            comment_list.like.add(request.user)
            return Response({"message":"이 댓글을 좋아합니다"}, status=status.HTTP_201_CREATED)

#대댓글 추가
class NestedCommentCreatetView(APIView):
    def post(self, request, product_id, comment_id):
        serializer = NestedCommentCreateSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product_id=product_id, comment_id=comment_id, user=request.user)
            return Response({"data":serializer.data,"message":"대댓글 등록 완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors":serializer.errors,"message":"대댓글 등록 실패"}, status=status.HTTP_400_BAD_REQUEST)

#대댓글 수정 및 삭제
class NestedCommentDetailView(APIView):
    def put(self, request, product_id, comment_id, nestedcomment_id):
        nested_comment = get_object_or_404(Nested_Comment, id=comment_id)
        serializer = NestedCommentCreateSerializer(nested_comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(id=nestedcomment_id, product_id=product_id, comment_id=comment_id, user=request.user)
            return Response({"message": "해당 대댓글이 수정되었습니다.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, product_id, comment_id, nestedcomment_id):
        nested_comment = Nested_Comment.objects.filter(Q(id=nestedcomment_id)&Q(product_id=product_id)&Q(comment_id=comment_id)&Q(user_id=request.user.id))
        nested_comment.delete()
        return Response({"message": "해당 대댓글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)