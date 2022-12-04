from django.urls import path
from . import views

urlpatterns = [
    
    path('survey/', views.SurveyStart.as_view(), name='survey'),

]