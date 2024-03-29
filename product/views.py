import pandas as pd
from product.models import Product, Cart
from product.serializers import ViewProductSerializer,ProductCreateSerializer, ProductDetailSerializer, CartSaveSerializer, CartViewSerializer, ProductDetailEditSerializer
from .pagination import PageNumberPagination, get_pagination_result
from user.models import UserModel
from machine.recommend import recommend_products, save_dataframe, recommend_start
from survey.serializers import ShowProductSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.db.models import Q
# Create your views here.



class MainpageView(APIView):

    def get(self, request):
        data = {}
        recommend = []
        category = ["coffee", "goods", "product"]

        for i in range(3):
            product = Product.objects.filter(category=i+1).order_by('?')[:10]
            serializer = ViewProductSerializer(product, many=True)
            data[category[i]] = serializer.data
        if request.user.is_authenticated == True :
            user = UserModel.objects.get(id=request.user.id)
            survey = user.user_survey.all()
            if survey :
                survey = survey.order_by('-id')[0]
                aroma = survey.aroma_grade
                acidity = survey.acidity_grade
                sweetness = survey.sweet_grade
                balance = survey.body_grade

                user_survey = recommend_start(aroma, acidity, sweetness, balance)
                for i in range(len(user_survey)):
                    product = get_object_or_404(Product, product_name = user_survey[i])
                    survey_data = ShowProductSerializer(product)
                    recommend.append(survey_data.data)
            else :
                pass


        return Response({"data":data, "recommend":recommend}, status=status.HTTP_201_CREATED)

class MainTypeView(APIView):

    def get(self, request):
        category = int(request.GET.get('category_id', None))
        sort = request.GET.get('sort', None)
        print(sort)

        if category == 1:
            products = Product.objects.filter(category=category).order_by("-created_at")
        elif category == 2:
            products = Product.objects.filter(category=category).order_by("-id")
        elif category == 3:
            products = Product.objects.filter(category=category).order_by("-created_at")
        elif category == 4:
            if sort=='up':
                products = Product.objects.filter(category=1).order_by("body_grade")
            else :
                products = Product.objects.filter(category=1).order_by("-body_grade")
        elif category == 5:
            if sort=='up':
                products = Product.objects.filter(category=1).order_by("acidity_grade")
            else :
                products = Product.objects.filter(category=1).order_by("-acidity_grade")
        else :
            return Response({"message":"카테고리 넘버 이상"}, status=status.HTTP_400_BAD_REQUEST)

        paginator = PageNumberPagination()
        p = paginator.paginate_queryset(queryset=products, request=request)
        paging = get_pagination_result(paginator, products.count())
        serializer = ViewProductSerializer(p, many=True)
        return Response({"data": serializer.data, "page":paging}, status=status.HTTP_200_OK)

class ProductCreateView(APIView):
    permission_classes=[permissions.IsAdminUser]

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
            # 추천 상품 불러오기
        if product.category_id == 1:
            rec_product_id_list = product.recommend_product
            rec_product_id = rec_product_id_list.split("|")
            rec_data = {}
            for i,id in enumerate(rec_product_id):
                product = get_object_or_404(Product, id=id)
                rec_serializer = ViewProductSerializer(product)
                rec_data[i] = rec_serializer.data
            return Response({"products":serializer.data, "recommend":rec_data}, status=status.HTTP_200_OK)

        else :
            rec_etc_data = {}
            rec_etc_products = Product.objects.filter(category_id=product.category_id).order_by("?")[:7]
            for i,name in enumerate(rec_etc_products):
                product = get_object_or_404(Product, id=name.id)
                rec_serializer = ViewProductSerializer(product)
                rec_etc_data[i] = rec_serializer.data
            return Response({"products":serializer.data,"recommend":rec_etc_data}, status=status.HTTP_200_OK)

class ProductRecomendSave(APIView):
    permission_classes = [permissions.IsAdminUser]
    def post(self, request):
        product_list = Product.objects.all()
        for pro in product_list:
            product = get_object_or_404(Product, id=pro.id)
                # 추천 상품 불러오기
            if product.category_id == 1:
                rec_product_list = recommend_products(product.product_name)
                rec_products = []
                for name in rec_product_list:
                    rec_product = get_object_or_404(Product, product_name=name)
                    rec_products.append(str(rec_product.id))
                rec_products = '|'.join(rec_products)
                setattr(product,"recommend_product",rec_products)
                product.save()
            else :
                pass
        return Response({"message":"추천상품 등록 완료"}, status=status.HTTP_200_OK)


    def put(self, request):
        product_id = int(request.GET.get('product_id', None))
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductDetailEditSerializer(product, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정되었습니다.", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.error})

    def delete(self, request):
        product_id = int(request.GET.get('product_id', None))
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return Response({"message":"게시글이 삭제 되었습니다."}, status=status.HTTP_200_OK)

class ProductSearchView(APIView):

    def get(self, request):
        search = request.GET.get("search")
        products = Product.objects.filter(Q(product_name__contains=search)|Q(content__contains=search)).order_by('-created_at')
        paginator = PageNumberPagination()
        p = paginator.paginate_queryset(queryset=products, request=request)
        paging = get_pagination_result(paginator, products.count())
        serializer = ViewProductSerializer(p, many=True)
        return Response({"data": serializer.data, "page":paging}, status=status.HTTP_200_OK)

class ProductLikeView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.GET.get("product_id")
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
        product = Product.objects.get(id=product_id)
        request.data._mutable = True
        request.data["product_image"] = product.image
        serializer = CartSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user= request.user, product_id=product_id)
            return Response({"message":"장바구니에 추가하였습니다", "data":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        cart_id = request.GET.get('cart_id', None)
        cart = Cart.objects.filter(id = cart_id)
        if cart:
            cart.delete()
            return Response({"message":"장바구니에서 삭제되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"해당 물품은 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

class ProductSave(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request):
        products = Product.objects.all()
        id = []
        product_name = []
        aroma_grade = []
        acidity_grade = []
        sweet_grade = []
        body_grade = []
        for product in products:
            if product.category.id == 1:
                id.append(product.id)
                product_name.append(product.product_name)
                aroma_grade.append(product.aroma_grade)
                acidity_grade.append(product.acidity_grade)
                sweet_grade.append(product.sweet_grade)
                body_grade.append(product.body_grade)
        newdata = {}
        newdata["num"]=id
        newdata["name_ko"]=product_name
        newdata["aroma_grade"]=aroma_grade
        newdata["acidity_grade"]=acidity_grade
        newdata["sweet_grade"]=sweet_grade
        newdata["body_grade"]=body_grade
        df = pd.DataFrame(newdata)
        df.to_csv("./machine/dbdata.csv", index=False, encoding='cp949')
        save_dataframe()

        return Response({"message":"저장되었습니다."}, status=status.HTTP_200_OK)