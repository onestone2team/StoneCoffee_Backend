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

        # return Response({"order_data":order_serializer.data,"payment_data":payment_serializer.data}, status=status.HTTP_200_OK)
        return Response({"message":"주문되었습니다."}, status=status.HTTP_200_OK)

class order_cancel(APIView):

    def post(self, request):

        cancel_order_id = request.GET.get("order_id", None).split(",")

        only_one_order = get_object_or_404(Order, id=int(cancel_order_id[0]))
        only_one_order_product_price = only_one_order.order_price
        only_one_order_count = only_one_order.count
        only_one_payment_id = only_one_order.payment_num_id
        only_one_order_price = only_one_order_count * only_one_order_product_price
        payment = get_object_or_404(Payment, id=only_one_payment_id)
        payment_price = int(payment.total_price)

        if only_one_order_price == 0 or payment_price ==0:
            return Response({"message":"잘못된 취소요청 입니다"}, status=status.HTTP_400_BAD_REQUEST)

        elif only_one_order_price == payment_price:

            if only_one_order.status == 3 or payment.status == 3:
                return Response({"message":"이미 취소된 주문입니다"}, status=status.HTTP_400_BAD_REQUEST)

            else:
                setattr(payment, "status", 3)
                setattr(only_one_order, "status", 3)
                payment.save()
                only_one_order.save()
                return Response({"message":"주문취소 요청이 완료되었습니다."}, status=status.HTTP_200_OK)

        elif only_one_order_price != payment_price:
            cancel_price = 0
            for id in cancel_order_id:
                order = get_object_or_404(Order, id=id)
                payment_id = order.payment_num_id
                payment = get_object_or_404(Payment, id=payment_id)
                payment_price = int(payment.total_price)

                if order.status == 3 or payment.status == 3:
                    order_product_name = order.product_name
                    return Response({"message":f"{order_product_name}은 이미 취소된 주문입니다"}, status=status.HTTP_400_BAD_REQUEST)

                else:
                    cancel_product_price = order.order_price
                    cancel_product_count = order.count
                    cancel_price += cancel_product_price * cancel_product_count
                    price = payment_price - cancel_price

                if price < 50000 and payment_price-3000 < 50000:
                    return Response({"message":"주문금액이 5만원 이하입니다. 배송비 3000원 추가 결제 부탁드립니다.", "need":"배송비결제"}, status=status.HTTP_200_OK)

                else:
                    setattr(order, "status", 3)
                    setattr(payment, "status", 3)
                    payment.save()
                    order.save()
                    return Response({"message":"주문취소 요청이 완료되었습니다."}, status=status.HTTP_200_OK)

        else:
            return Response({"message":"취소할 주문내역이 없습니다"}, status=status.HTTP_400_BAD_REQUEST)
