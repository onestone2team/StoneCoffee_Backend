from order import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('product/<int:product_id>/', views.UserOrderView.as_view(), name="user_product_view"),
    # path('product/<int:product_id>/', views.UserOrderListView.as_view(), name="user_product_view"),
]
