from django.urls import path
from mypage import views


urlpatterns = [
    path('profile/', views.ChangeUserInfo.as_view(), name='change_user_info_view'),
    path('profile/password/', views.ChangeUserPassword.as_view(), name='change_user_password'),
    path('bookmark/', views.ViewBookmarkList.as_view(), name='user_bookmark'),
    path('orderlist/', views.MyOrderListView.as_view(), name='change_user_info_view'),
    path('inquiry/', views.InquiryList.as_view(), name='inquiry_list'),
    path('inquiry/detail/', views.InquiryDetail.as_view(), name='inquiry_detail'),
    path('mypayment/', views.UserPaymentView.as_view(), name="user_product_view"),
]