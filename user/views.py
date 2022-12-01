from rest_framework.views import APIView
from user.models import UserModel
from rest_framework import status
from rest_framework.response import Response
from user.serializers import MyTokenObtainPairSerializer, SignUpSerializer



# Create your views here.
class MyTokenObtainPairSerializer(APIView):
    serializer_class = MyTokenObtainPairSerializer
    pass



class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_vaild(raise_exception=True):
            serializer.save()
            return Response({"message":"회원가입이 되었습니다!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"회원가입이 실패했습니다!"}, status=status.HTTP_400_BAD_REQUEST)
