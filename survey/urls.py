from django.urls import path
from . import views

urlpatterns = [

<<<<<<< HEAD
    path('guest/', views.SurveyStart.as_view(), name='none_see'),
=======
>>>>>>> 85acd5b6682cac49d30aef8ec9b3cf8e2172b26a
    path('survey/', views.SurveyStart.as_view(), name='survey'),

]