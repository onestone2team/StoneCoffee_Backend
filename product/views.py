from rest_framework.views import APIView
from product.models import Product,Category
from product.serializers import ProductSerializer,ProductCreateSerializer,CategorySerializer,ProductDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from product.permissions import IsAdminOrAuthenticatedOrReadOnly,DeletePermissition
from django.db.models import Q
# Create your views here.

class MainTypeView(APIView):
    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 9
        pagination.page_query_param = "page"
        products = Product.objects.filter(hide_option=0).order_by("-created_at")
        print(request)
        if request == 0:
            products = Product.objects.filter(category_id=0).order_by("-created_at")
        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductSerializer(p, many=True)
        return Response({"data": serializer.data, "max_page": len(products)//9 + 1,"message": ""}, status=status.HTTP_200_OK,)
    
class ProductCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response({"data": serializer.data, "message": "생성이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductView(APIView):
    pass
class ProductLikeView(APIView):
    pass
