from rest_framework.views import APIView
from user.models import UserModel
from mypage.models import Inquiry
from rest_framework.response import Response
from user.serializers import ChangeUserInfoSerializer
from mypage.serializers import InquiryListSerializer, AddinquiryListSerializer, AddadminInquirySerializer
from user.models import UserModel
from rest_framework import status
# Create your views here.

#사용자 문의
class InquiryList(APIView):
     def get(self, request):
        inquiry = Inquiry.objects.all()
        serializer = InquiryListSerializer(inquiry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddinquiryList(APIView):
     def post(self, request, category_id, product_id):
        serializer = AddinquiryListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category_id=category_id, product_id=product_id, user_id=request.user.id)
            return Response({"message": "문의가 등록되었습니다", "data": "serializer.data"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


#관리자 문의 페이지
class AdminInquiry(APIView):
    pass

class AddadminInquiry(APIView):
    pass


class ChangeUserInfo(APIView):

    def get(self, request):
        user = UserModel.objects.get(id=request.user.id)
        serializer = ChangeUserInfoSerializer(user)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        user = UserModel.objects.get(id=request.user.id)
        user_info = dict()
        for key,value in request.data.items():
            if value:
                user_info.update({key:value})
        serializer = ChangeUserInfoSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"data":serializer.data, "message":"변경이 완료되었습니다!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
