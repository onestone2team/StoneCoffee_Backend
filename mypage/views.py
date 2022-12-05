from rest_framework.views import APIView
from user.models import UserModel
from rest_framework.response import Response
from user.serializers import ChangeUserInfoSerializer
from user.models import UserModel
from rest_framework import status
from order.models import Order
from order.serializers import MyOrderListSerializer
from django.db.models import Q
from mypage.serializers import MyPaymentListSerializer
from django.db.models.sql.query import Query
from order.models import Payment

# Create your views here.

#사용자 문의
class InquiryList(APIView):
    pass


#관리자 문의 페이지
class DirectorInquiry(APIView):
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

class MyOrderListView(APIView):

    def get(self, request):
        orders = Order.objects.filter(user_id=request.user.id)
        serializer = MyOrderListSerializer(orders, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)


class UserPaymentView(APIView):

    def post(self, request):
        order_sets = Order.objects.filter(user_id=request.user.id)
        list_payment = Payment()
        for order in order_sets[0:]:
            for field in ["product_name", "order_price", "count", "user_name","weight" ,"receiver","user_address","user_phone", "status"]:
                if getattr(list_payment, field) == None:
                    add_payment = f"{getattr(order, field)}"
                    setattr(list_payment, field, add_payment)
                elif field in ["receiver","user_address","user_phone", "status"]:
                    pass
                else:
                    add_payment = f"{getattr(list_payment, field)}|{getattr(order, field)}"
                    setattr(list_payment, field, add_payment)
        count_list = getattr(list_payment, "count").split("|")
        price_list = getattr(list_payment, "order_price").split("|")
        total_price = 0
        for count in count_list:
            for price in price_list:
                total_price += int(count) * int(price)
        setattr(list_payment, "total_price", str(total_price))
        list_payment.save()
        return Response(status=status.HTTP_200_OK)







        # if serializer.is_valid():
        #     print(serializer.data)
        #     serializer.save()
        #     return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)