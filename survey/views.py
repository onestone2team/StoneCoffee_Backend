from .serializers import SurveySerializer, ShowProductSerializer
from machine.recommend import recommend_start
from product.models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Create your views here.
class SurveyStart(APIView):
    def post(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated == True :
                serializer.save(user = request.user)
            Aroma = serializer.data["aroma_grade"]
            Acidity = serializer.data["sweet_grade"]
            Sweetness = serializer.data["acidity_grade"]
            Balance = serializer.data["body_grade"]
            data = recommend_start(Aroma, Acidity, Sweetness, Balance)

            product = get_object_or_404(Product, product_name = data[0])
            productserializer1 = ShowProductSerializer(product)
            product = get_object_or_404(Product, product_name = data[1])
            productserializer2 = ShowProductSerializer(product)
            product = get_object_or_404(Product, product_name = data[2])
            productserializer3 = ShowProductSerializer(product)

            return Response({"data": {"1":productserializer1.data,"2": productserializer2.data,"3": productserializer3.data}}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"다시 시도해주세요"}, status=status.HTTP_400_BAD_REQUEST)


