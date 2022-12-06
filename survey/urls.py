from django.urls import path
from . import views

urlpatterns = [

    path('', views.SurveyStart.as_view(), name='survey'),

]