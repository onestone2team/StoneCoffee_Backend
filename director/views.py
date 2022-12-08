from product.models import Product
from order.models import Order
from mypage.models import Inquiry
from .serializers import AdminProductView, AdminProductStatusEdit, AddadminInquirySerializer
from mypage.serializers import InquiryListSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Create your views here.

class AdminOrderList(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        orders = Order.objects.all()
        serializer = AdminProductView(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        order_id = request.GET.get("order_id",None)
        order = Order.objects.get(id=order_id)
        serializer = AdminProductStatusEdit(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"messgae":"주문 상태 변경 완료", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'데이터 이상'}, status=status.HTTP_400_BAD_REQUEST)
#관리자 문의 페이지
class AdminInquiry(APIView):
    permission_classes=[permissions.IsAdminUser]
    def get(self, request):
        inquiry = Inquiry.objects.all().order_by('status','created_at')
        serializer = InquiryListSerializer(inquiry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)     

    def put(self, request):
        Inquiry_id = request.GET.get("Inquiry_id", None)
        inquiry = Inquiry.objects.get(id=Inquiry_id)
        if request.data['answer'] != "":
            serializer = AddadminInquirySerializer(inquiry, data=request.data)
        else:
            return Response({"message":"답변을 달아주세요"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save(status=True)
            return Response({"message":"답변을 달았습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    

    

