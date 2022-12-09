from product import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    # 홈페이지 간단한 소개
    path('',views.MainpageView.as_view()),
    # 카테고리 선택 (type= 1(coffeebean),2=(goods),3=(coffeemachine))
    path('category/', views.MainTypeView.as_view()),
    # 작성은 admin만 가능
    path('create/',views.ProductCreateView.as_view()),
    # # 게시글(제품) 조회
    path('detail/',views.ProductView.as_view()),
    # 게시글 좋아요
    path('<int:product_id>/like/',views.ProductLikeView.as_view()),
    # 게시글 장바구니
    path('cart/',views.ProductCartList.as_view()),

    path('order/',views.ProductCartList.as_view())
]

