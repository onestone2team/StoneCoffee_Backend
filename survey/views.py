from .serializers import GuestIpSerializer
from .models import Guest
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SurveyStart(APIView):
    def post(self, request):
        pass

