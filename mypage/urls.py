from django.urls import path
from mypage import views


urlpatterns = [
    path('inquiry/', views.InquiryList.as_view(), name='InquiryList'),
    path('director/inquiry/', views.DirectorInquiry.as_view(), name='DirectorInquiry'),
    path('changeuserinfo/', views.ChangeUserInfo.as_view(), name='change_user_info_view'),
    path('myorderlist/', views.MyOrderListView.as_view(), name='change_user_info_view'),
]