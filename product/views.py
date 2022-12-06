from product.models import Product,Category, Cart
from product.serializers import ProductSerializer, ViewProductSerializer,ProductCreateSerializer, CategorySerializer,ProductDetailSerializer, CartSaveSerializer, CartViewSerializer
from .pagination import PageNumberPagination, get_pagination_result
from rest_framework import status, generics, permissions
from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from product.permissions import IsAdminOrAuthenticatedOrReadOnly,DeletePermissition
from django.db.models import Q
# Create your views here.



class MainpageView(APIView):

    def get(self, request):
        data = {}
        category = ["coffee", "goods", "product"]
        for i in range(3):
            product = Product.objects.filter(category=i+1).order_by('-created_at')[:10]
            serializer = ViewProductSerializer(product, many=True)
            data[category[i]] = serializer.data

        return Response({"data":data}, status=status.HTTP_201_CREATED)
    
class MainTypeView(APIView):
    def get(self, request):
        category = int(request.GET.get('category_id', None))
        
        if category <= 3:
            products = Product.objects.filter(category=category).order_by("-created_at")
        elif category == 4:
            products = Product.objects.filter(category=1).order_by("-body_grade")
        elif category == 5:
            products = Product.objects.filter(category=1).order_by("-acidity_grade")
        else :
            return Response({"message":"카테고리 넘버 이상"}, status=status.HTTP_400_BAD_REQUEST)

        paginator = PageNumberPagination()
        paging = get_pagination_result(paginator, products.count())  
        p = paginator.paginate_queryset(queryset=products, request=request)
        serializer = ViewProductSerializer(p, many=True)
        return Response({"data": serializer.data, "page":paging}, status=status.HTTP_200_OK)
    
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
    def get(self, request):
        product_id = int(request.GET.get('product_id', None))
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductDetailSerializer(product)
        return Response({"products":serializer.data}, status=status.HTTP_200_OK)
    
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
     
