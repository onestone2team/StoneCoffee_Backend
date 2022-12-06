from django.urls import path
from mypage import views


urlpatterns = [
    path('mypage/inquiry/', views.InquiryList.as_view(), name='InquiryList'),
    path('mypage/<int:user_id>/<int:category_id>/<int:product_id>/inquiry/', views.AddinquiryList.as_view(), name='AddinquiryList'),
    path('mypage/admin/inquiry/', views.AdminInquiry.as_view(), name='DirectorInquiry'),
    path('mypage/admin/inquiry/<int:Inquiry_id>/', views.AddadminInquiry.as_view(), name='AddadminInquiry'),
    path('changeuserinfo/', views.ChangeUserInfo.as_view(), name='change_user_info_view'),
]