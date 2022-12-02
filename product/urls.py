from product import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    # 홈페이지 간단한 소개
    path('',),
    # 카테고리 선택 (type= 0(coffeebean),1=(goods),2=(coffeemachine))
    path('<int:type_id>/', views.MainTypeView.as_view()),
    # 작성은 admin만 가능
    path('create/',views.ProductCreateView.as_view()),
    # # 게시글(제품) 조회
    path('<int:product_id>/view/',views.ProductView.as_view()),
    # 게시글 좋아요
    path('<int:product_id>/bookmark/',views.ProductLikeView.as_view())
    
]

