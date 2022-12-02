from django.urls import path
from . import views


app_name = 'comment'

urlpatterns = [
    # 댓글
    path('<int:product_id>/comment/',views.CommentCreateView.as_view(), name='create_comment'),
    path('<int:product_id>/comment/<int:comment_id>/',views.CommentDetailView.as_view(), name='read_comment'),
    path('<int:product_id>/comment/<int:comment_id>/',views.CommentDetailView.as_view(), name='put_comment'),
    path('<int:product_id>/comment/<int:comment_id>/delete/',views.CommentDetailView.as_view(), name='delete_comment'),
    path('<int:product_id>/comment/<int:comment_id>/like/',views.CommentLikeView.as_view(), name='like_comment'),
    # 대댓글
    path('<int:product_id>/comment/<int:comment_id>/',views.NestedCommentCreatetView.as_view(), name='create_nestedcomment'),
    path('<int:product_id>/comment/<int:comment_id>/<int:nestedcomment_id>/',views.NestedCommentDetailView.as_view(), name='put_nestedcomment'),
    path('<int:product_id>/comment/<int:comment_id>/<int:nestedcomment_id>/delete/',views.NestedCommentDetailView.as_view(), name='delete_nestedcomment'),

]
