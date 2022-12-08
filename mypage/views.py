from user.models import UserModel
from mypage.models import Inquiry
from order.models import Order, Payment
from product.models import Product
from order.serializers import MyOrderListSerializer
from mypage.serializers import MyPaymentListSerializer, InquiryListSerializer, AddinquiryListSerializer, InquiryDetailSerializer
from user.serializers import ChangeUserInfoSerializer, ChangeUserPasswordSerializer
from product.serializers import ViewProductSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

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
#비밀번호 변경
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
#북마크 리스트
class ViewBookmarkList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        coffees = Product.objects.filter(Q(category_id=1)&Q(like=request.user.id)).order_by('liketage')
        coffees_serializer = ViewProductSerializer(coffees, many=True)
        products = Product.objects.exclude(category_id=1) & Product.objects.filter(like=request.user.id).order_by('liketage')
        products_serializer = ViewProductSerializer(products, many=True)
        return Response({"coffee": coffees_serializer.data, "product":products_serializer.data}, status=status.HTTP_200_OK)
#주문 리스트
class MyOrderListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        orders = Order.objects.filter(user_id=request.user.id).order_by('-created_at')
        serializer = MyOrderListSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
#사용자 문의
class InquiryList(APIView):
    def get(self, request):
        inquiry = Inquiry.objects.filter(user=request.user.id)
        serializer = InquiryListSerializer(inquiry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product_id = request.GET.get("product_id",None)
        serializer = AddinquiryListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product_id=product_id, user_id=request.user.id)
            return Response({"message": "문의가 등록되었습니다", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#사용자 문의 디테일 페이지
class InquiryDetail(APIView):
    def get(self, request):
        inquiry_id = request.GET.get("inquiry_id",None)
        inquiry = get_object_or_404(Inquiry,id=inquiry_id)
        serializer = InquiryDetailSerializer(inquiry)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserPaymentView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        payments = Payment.objects.filter(user_id=request.user.id)
        serializer = MyPaymentListSerializer(payments, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

