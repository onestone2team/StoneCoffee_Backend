from django.urls import path
from . import views

urlpatterns = [

    path('guest/', views.SurveyStart.as_view(), name='none_see'),
    path('survey/', views.SurveyStart.as_view(), name='survey'),

]