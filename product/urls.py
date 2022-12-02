from product import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    # 홈페이지 간단한 소개
    path('',),
    # 카테고리 선택 (type= 0(coffeebean),1=(goods),2=(coffeemachine))
    path('<int:type_id>/', views.ProductView.as_view()),
    # 작성은 admin만 가능
    path('create/',views.ProductView.as_view()),
    # # 게시글(제품) 조회
    path('view/<int:product_id>/',views.ProductView.as_view()),
    
]

