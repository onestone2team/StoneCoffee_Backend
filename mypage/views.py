from rest_framework.views import APIView
from user.models import UserModel
from mypage.models import Inquiry
from rest_framework.response import Response
from user.serializers import ChangeUserInfoSerializer, ChangeUserPasswordSerializer
from mypage.serializers import InquiryListSerializer, AddinquiryListSerializer, AddadminInquirySerializer
from user.models import UserModel
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from order.models import Order
from order.serializers import MyOrderListSerializer
from mypage.serializers import MyPaymentListSerializer
from order.models import Payment
from rest_framework import permissions

# Create your views here.

#개인 프로필 보기
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

class ChangeUserPassword(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = UserModel.objects.get(id=request.user.id)
        serializer = ChangeUserPasswordSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"비밀번호가 변경 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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
    def get(self, request):
        inquiry = Inquiry.objects.all()
        serializer = InquiryListSerializer(inquiry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddadminInquiry(APIView):
    permission_classes=[IsAuthenticated]

    
    def put(self, request, Inquiry_id):
        inquiry = Inquiry.objects.get(id=Inquiry_id)
        serializer = AddadminInquirySerializer(inquiry,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MyOrderListView(APIView):
    permission_classes = (permissions.IsAuthenticated)

    def get(self, request):
        orders = Order.objects.filter(user_id=request.user.id)
        serializer = MyOrderListSerializer(orders, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)


class UserPaymentView(APIView):
    permission_classes = (permissions.IsAdminUser)

    def get(self, request):
        payments = Payment.objects.filter(user_id=request.user.id)
        serializer = MyPaymentListSerializer(payments, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

