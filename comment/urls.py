from django.urls import path
from . import views


urlpatterns = [
    # 댓글
    path('<int:product_id>/comment/',views.CommentCreateView.as_view(), name='create_comment'),
    path('<int:product_id>/comment/<int:comment_id>/',views.CommentDetailView.as_view(), name='read_comment'),
    path('<int:product_id>/comment/<int:comment_id>/like/',views.CommentLikeView.as_view(), name='like_comment'),
    # 대댓글
    path('nested/<int:product_id>/comment/<int:comment_id>/',views.NestedCommentCreatetView.as_view(), name='create_nestedcomment'),
    path('nested/<int:product_id>/comment/<int:comment_id>/<int:nestedcomment_id>/',views.NestedCommentDetailView.as_view(), name='put_nestedcomment'),

]
