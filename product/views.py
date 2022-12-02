from rest_framework.views import APIView
from product.models import Products, Comments, Categories
from product.serializers import asd
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from product.permissions import asd
# Create your views here.

class MainTypeView(APIView):
    pass
class ProductCreateView(APIView):
    pass
class ProductView(APIView):
    pass
class ProductLikeView(APIView):
    pass
