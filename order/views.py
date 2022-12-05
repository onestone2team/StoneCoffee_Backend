from rest_framework import status
from rest_framework.views import APIView
from order.models import Order, Payment
from order.serializers import UserOrderCreateSerializer
from rest_framework.response import Response
from django.db.models import Q
from product.models import Product, Cart
from django.forms.models import model_to_dict


# address = re.compile("(([가-힣A-Za-z·\d~\-\.]{2,}(로|길).[\d]+)|([가-힣A-Za-z·\d~\-\.]+(읍|동)\s)[\d]+)")
# Create your views here.


class UserOrderView(APIView):

    def post(self, request):
        cart_id = request.GET.get("cart_id", None).split(",")
        for cart in cart_id:
            product = Cart.objects.get(id=cart)
            print(product.product.price)
            product = model_to_dict(product)
            del(product["user"])
            product["order_price"] = product.pop("price")
            user_data = request.data
            for data in user_data:
                product[f"{data}"] = user_data[f"{data}"]
            serializer = UserOrderCreateSerializer(data=product)
            if serializer.is_valid():
                serializer.save(user_id=request.user.id, user_name=request.user)
                return Response({"message":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
