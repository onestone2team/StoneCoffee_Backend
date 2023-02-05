from user import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path("login/", views.MyTokenObtainPairSerializer.as_view(), name="login_view"),
    path("signup/", views.SignUpView.as_view(), name="signup_view"),
    path("userdata/", views.UserData.as_view(), name="user_data_view"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('kakao/request/', views.KakaoView().as_view(), name='kakao_login'),
    path('kakao/callback/', views.KakaoTokenGet().as_view(), name='kakao_token'),
]
