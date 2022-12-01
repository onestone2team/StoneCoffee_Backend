from django.urls import path
from . import views


app_name = 'comment'

urlpatterns = [
    # 댓글
    path('',views.CommentDetailView.as_view(), name='comment_detail'),
    path('<int:product_id>/comment/',views.AddCommentView.as_view(), name='add_comment'),
    path('<int:product_id>/comment/<int:comment_id>/',views.PutCommentView.as_view(), name='put_comment'),
    path('<int:product_id>/comment/<int:comment_id>/delete/',views.DeleteCommentView.as_view(), name='delete_comment'),
    path('<int:product_id>/comment/<int:comment_id>/like/',views.CommentLikeView.as_view(), name='comment_like'),
    # 대댓글
    path('<int:product_id>/comment/<int:comment_id>/',views.AddCommentView.as_view(), name='add_nestedcomment'),
    path('<int:product_id>/comment/<int:comment_id>/<int:nestedcomment_id>/',views.PutCommentView.as_view(), name='put_nestedcomment'),
    path('<int:product_id>/comment/<int:comment_id>/<int:nestedcomment_id>/delete/',views.DeleteCommentView.as_view(), name='delete_nestedcomment'),

]
