from director import views
from django.urls import path

urlpatterns = [

    path('order/', views.AdminOrderList.as_view(), name="admin_order_view"),
    path('inquiry/', views.AdminInquiry.as_view(), name='director_inquiry'),

]