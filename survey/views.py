from .models import Survey
from .serializers import SurveySerializer
from .machine.recommend import recommend_start
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SurveyStart(APIView):
    def post(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            Aroma = serializer.data["aroma_grade"]
            Acidity = serializer.data["sweet_grade"]
            Sweetness = serializer.data["acidity_grade"]
            Balance = serializer.data["body_grade"]
            data = recommend_start(Aroma, Acidity, Sweetness, Balance)

            return Response({"message": data}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"다시 시도해주세요"}, status=status.HTTP_400_BAD_REQUEST)


