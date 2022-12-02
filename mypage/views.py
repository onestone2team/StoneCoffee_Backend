from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from mypage.models import Inquiry
from mypage.serializers import InquiryListSerializer
# Create your views here.

#사용자 문의
class InquiryList(APIView):
    def get(self,request):
     inquiry = Inquiry.objects.all()  
     serializer = InquiryListSerializer(inquiry, many=True) 
     return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        pass

#관리자 문의 페이지
class DirectorInquiry(APIView):
    pass


class ChangeUserInfo(APIView):
    pass