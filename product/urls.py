from product import views
from django.urls import path


urlpatterns = [
    path('',views.MainpageView.as_view()),                  # 홈페이지 간단한 소개
    path('category/', views.MainTypeView.as_view()),        # 카테고리 선택 (type= 0(coffee),1=(goods),2=(etc))
    path('create/',views.ProductCreateView.as_view()),      # 작성은 admin만 가능
    path('detail/',views.ProductView.as_view()),            # 게시글(제품) 조회
    path('like/',views.ProductLikeView.as_view()),          # 게시글 좋아요
    path('search/', views.ProductSearchView.as_view()),
    path('cart/',views.ProductCartList.as_view()),          # 게시글 장바구니
    path('save/',views.ProductSave.as_view()),
    path('recomend/',views.ProductRecomendSave.as_view()),
    
]

