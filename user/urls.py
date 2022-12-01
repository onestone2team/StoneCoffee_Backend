from user import views
from django.urls import path
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login_view"),
    path("signup/", views.SignUpView.as_view(), name="signup_view"),
    path("logout/", views.LogOutView.as_view(), name="logout_view"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
