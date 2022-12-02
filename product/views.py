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
class MainpageView(APIView):
    def get(self,request):
        pagination = PageNumberPagination()
        products = Product.objects.order_by("?")
        # "?"은 랜덤으로 나열하는 함수입니다.
        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductSerializer(p,many=True)
        return Response({"data":serializer.data,"message": "메인페이지 불러오기 성공"}, status=status.HTTP_201_CREATED)
        
    
    
class MainTypeView(APIView):
    def get(self, request,type_id):
        pagination = PageNumberPagination()
        pagination.page_size = 9
        pagination.page_query_param = "page"
        products = Product.objects.filter(type=type_id).order_by("id")
        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductSerializer(p, many=True)
        print(serializer.data)
        return Response({"data": serializer.data, "max_page": len(products)//9 + 1}, status=status.HTTP_200_OK,)
    
class ProductCreateView(APIView):
    # permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response({"data": serializer.data, "message": "생성이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ProductLikeView(APIView):
    # permission_classes=[permissions.IsAuthenticated]

    def post(self, request, product_id):
        like_list = get_object_or_404(Product, id=product_id)
        if request.user in like_list.like.all():
            like_list.like.remove(request.user)
            return Response({"message":"북마크에 삭제되었습니다"}, status=status.HTTP_200_OK)
        else:
            like_list.like.add(request.user)
            return Response({"message":"북마크에 추가하였습니다"}, status=status.HTTP_202_ACCEPTED)
