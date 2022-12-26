from order import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('product/order/', views.UserOrderCreateView.as_view(), name="user_product_view"),
    path('product/order_cancel/', views.order_cancel.as_view(), name="user_order_cancel_view"),
    # path('product/<int:product_id>/', views.UserOrderListView.as_view(), name="user_product_view"),
]
