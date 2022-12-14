from rest_framework.views import APIView
from .models import Comment, Nested_Comment
from .serializers import CommentSerializer, CommentCreateSerializer, NestedCommentCreateSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404


#댓글 추가
class CommentCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self, request):
        product_id = request.GET.get('product_id')
        comment = Comment.objects.filter(Q(product_id=product_id)&Q(user_id=request.user.id))
        if comment.count()<1:
            serializer = CommentCreateSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(product_id=product_id, user=request.user)
                return Response({"data":serializer.data,"message":"댓글이 등록되었습니다."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"errors":serializer.errors,"message":"댓글이 정상적으로 등록되지 않았습니다. 다시 시도해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"댓글은 게시물당 하나씩만 등록할 수 있습니다."}, status=status.HTTP_400_BAD_REQUEST)

#댓글 및 대댓글 조회, 댓글 수정 및 삭제
class CommentDetailView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        comment_id = request.GET.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    def put(self, request):
        comment_id = request.GET.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentCreateSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "해당 댓글이 수정되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        comment_id = request.GET.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return Response({"message": "해당 댓글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

#좋아요
class CommentLikeView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        comment_id = request.GET.get('comment_id')
        comment_list = get_object_or_404(Comment, id=comment_id)
        if request.user in comment_list.like.all():
            comment_list.like.remove(request.user)
            return Response({"message":"좋아요를 취소했습니다."}, status=status.HTTP_200_OK)
        else:
            comment_list.like.add(request.user)
            return Response({"message":"이 댓글을 좋아합니다"}, status=status.HTTP_201_CREATED)

#대댓글 추가
class NestedCommentCreatetView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        comment_id = request.GET.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        serializer = NestedCommentCreateSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product_id=comment.product.id, comment_id=comment_id, user=request.user)
            return Response({"data":serializer.data,"message":"대댓글이 등록되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors":serializer.errors,"message":"대댓글이 정상적으로 등록되지 않았습니다. 다시 시도해주세요."}, status=status.HTTP_400_BAD_REQUEST)

#대댓글 수정 및 삭제
class NestedCommentDetailView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def put(self, request):
        nestedcomment_id = request.GET.get('nestedcomment_id')
        nested_comment = get_object_or_404(Nested_Comment, id=nestedcomment_id)
        serializer = NestedCommentCreateSerializer(nested_comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"data": serializer.data, "message": "해당 대댓글이 수정되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors":serializer.errors, "message": "대댓글이 정상적으로 수정되지 않았습니다. 다시 시도해주세요."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        nestedcomment_id = request.GET.get('nestedcomment_id')
        nested_comment = Nested_Comment.objects.get(id=nestedcomment_id)
        nested_comment.delete()
        return Response({"message": "해당 대댓글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)