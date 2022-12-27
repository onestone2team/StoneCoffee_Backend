from rest_framework import status
from rest_framework.views import APIView
from order.models import Payment, OrderCancel
from product.models import Product
from order.serializers import UserOrderCreateSerializer, PaymentSerialzier
from rest_framework.response import Response
from order.models import Order
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
            cart = Cart.objects.get(id=cart)
            product = model_to_dict(cart)
            user_data = request.data
            data = payment_serializer.data
            product["payment_num"] = payment.id
            product["product_name"] = cart.product.product_name
            product["order_price"] = product.pop("price")
            for data in user_data:
                product[f"{data}"] = user_data[f"{data}"]
            order_serializer = UserOrderCreateSerializer(data=product)
            if order_serializer.is_valid():
                order_serializer.save(user_name=request.user, product_id=product["product"])
                cart.delete()
            else:
                return Response({"order_error":order_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message":"주문되었습니다."}, status=status.HTTP_200_OK)

class order_cancel(APIView):

    def post(self, request):

        cancel_order_id = request.GET.get("order_id", None)
        order = get_object_or_404(Order, id=int(cancel_order_id))
        order_product_price = order.order_price
        order_count = order.count
        payment_id = order.payment_num_id
        order_price = order_count * order_product_price
        payment = get_object_or_404(Payment, id=payment_id)
        payment_price = payment.total_price
        payment_price = int(payment_price.replace(",",""))

        if order.status == 3 or payment.status == 3 or order.status == 4 or payment.status == 4:
            return Response({"message":f"{order.product_name}은 이미 취소된 주문입니다"}, status=status.HTTP_400_BAD_REQUEST)

        elif order.status != 3 or payment.status != 3 or order.status != 4 or payment.status != 4:
            
            
            if order_price == payment_price:  # 전체취소
                setattr(payment, "status", 3)
                setattr(order, "status", 3)
                payment.save()
                order.save()
                return Response({"message":"주문취소 요청이 완료되었습니다.","price":payment.total_price}, status=status.HTTP_200_OK)

            elif payment_price - 3000 > 50000 and payment_price - order_price < 50000: # 부분취소
                setattr(order, "status", 3)
                setattr(payment, "total_price", payment_price-order_price)
                payment.save()
                order.save()
                return Response({"message":"주문금액이 50000원 이하가 되어 배송비 3000원을 제외한 금액을 환불해 드립니다","price":order_price-3000}, status=status.HTTP_200_OK)

            else:
                setattr(order, "status", 3) #부분취소
                setattr(payment, "total_price", payment_price-order_price) # 
                payment.save()
                order.save()
                return Response({"message":"주문취소 요청이 완료되었습니다.","price":order_price}, status=status.HTTP_200_OK)

        else:
            return Response({"message":"취소할 주문내역이 없습니다"}, status=status.HTTP_400_BAD_REQUEST)


