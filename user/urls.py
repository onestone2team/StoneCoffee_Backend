from user import views
from django.urls import path
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path("login/", views.MyTokenObtainPairSerializer.as_view(), name="login_view"),
    path("signup/", views.SignUpView.as_view(), name="signup_view"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
