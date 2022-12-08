from django.urls import path
from . import views


urlpatterns = [
    # 댓글
    path('',views.CommentCreateView.as_view(), name='create_comment'),
    path('edit/',views.CommentDetailView.as_view(), name='read_comment'),
    path('like/',views.CommentLikeView.as_view(), name='like_comment'),
    # 대댓글
    path('nested/',views.NestedCommentCreatetView.as_view(), name='create_nestedcomment'),
    path('nested/edit/',views.NestedCommentDetailView.as_view(), name='put_nestedcomment'),

]
