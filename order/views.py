from rest_framework import status
from rest_framework.views import APIView
from order.models import Payment
from product.models import Product
from order.serializers import UserOrderCreateSerializer, PaymentSerialzier
from rest_framework.response import Response
from product.models import Cart
from django.forms.models import model_to_dict
from django.db.models import Q
from rest_framework.generics import get_object_or_404




class UserOrderCreateView(APIView):

    def post(self, request):
        cart_id = request.GET.get("cart_id", None).split(",")
        total_price = 0
        payment_data = dict()
        for cart in cart_id:
            product = Cart.objects.get(id=cart)
            product = model_to_dict(product)
            total_price += product["price"] * product["count"]
            payment_data["total_price"] = total_price
            payment_data["user"] = product["user"]
        payment_serializer = PaymentSerialzier(data=payment_data)
        if payment_serializer.is_valid():
            payment = payment_serializer.save()
        else:
            return Response({"error":payment_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        for cart in cart_id:
            product = Cart.objects.get(id=cart)
            product = model_to_dict(product)
            user_data = request.data
            data = payment_serializer.data
            payment_id = payment.id
            product_name = product.product.product_name
            product["payment_num"] = payment_id
            product["product_name"] = product_name
            product["order_price"] = product.pop("price")
            for data in user_data:
                product[f"{data}"] = user_data[f"{data}"]
            order_serializer = UserOrderCreateSerializer(data=product)
            if order_serializer.is_valid():
                order_serializer.save(user_name=request.user, product_id=product["product"])
            else:
                return Response({"order_error":order_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"order_data":order_serializer.data,"payment_data":payment_serializer.data}, status=status.HTTP_200_OK)