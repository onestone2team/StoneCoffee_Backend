from django.urls import path
from mypage import views


urlpatterns = [
    path('mypage/inquiry/', views.InquiryList.as_view(), name='InquiryList'),
    path('mypage/<int:user_id>/<int:category_id>/<int:product_id>/inquiry/', views.AddinquiryList.as_view(), name='AddinquiryList'),
    path('director/inquiry/', views.DirectorInquiry.as_view(), name='DirectorInquiry'),
    path('changeuserinfo/', views.ChangeUserInfo.as_view(), name='change_user_info_view'),
]