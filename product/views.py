from rest_framework.views import APIView
from product.models import Product,Category, Cart
from product.serializers import ProductSerializer,ProductCreateSerializer,CategorySerializer,ProductDetailSerializer, CartSaveSerializer, CartViewSerializer
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
        return Response({"data": serializer.data, "max_page": len(products)//9 + 1}, status=status.HTTP_200_OK,)
    
class ProductCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "생성이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ProductLikeView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, product_id):
        like_list = get_object_or_404(Product, id=product_id)
        if request.user in like_list.like.all():
            like_list.like.remove(request.user)
            return Response({"message":"좋아요 삭제되었습니다"}, status=status.HTTP_200_OK)
        else:
            like_list.like.add(request.user)
            return Response({"message":"좋아요에 담겼습니다."}, status=status.HTTP_202_ACCEPTED)

class ProductCartList(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        products = Cart.objects.filter(user_id=request.user.id)
        serializer = CartViewSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)     

    def post(self, request):
        product_id = request.GET.get('product_id', None)
        serializer = CartSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user= request.user, product_id=product_id)
            return Response({"message":"장바구니에 추가하였습니다", "data":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        cart_id = request.GET.get('cart_id', None)
        cart = Cart.objects.get(id = cart_id)
        if cart:
            cart.delete()
            return Response({"message":"장바구니에서 삭제되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"해당 물품은 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
     
