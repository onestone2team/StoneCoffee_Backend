from rest_framework import status
from rest_framework.views import APIView
from order.models import Order, Payment
from order.serializers import UserOrderCreateSerializer
from rest_framework.response import Response
from django.db.models import Q
from product.models import Product


# address = re.compile("(([가-힣A-Za-z·\d~\-\.]{2,}(로|길).[\d]+)|([가-힣A-Za-z·\d~\-\.]+(읍|동)\s)[\d]+)")
# Create your views here.


class MyOrderListView(APIView):

    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        serializer = UserOrderCreateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save(order_price=product.price, product_name=product.name, product_image=product.image, user_name=request.user)
            return Response({"message":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)