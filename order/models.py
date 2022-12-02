from django.db import models
from user.models import UserModel
from product.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_num = models.ForeignKey(Payment, verbose_name=("결제번호"), on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    order_price = models.IntegerField()
    count = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.IntegerField(verbose_name="주문 상태")
    user_name = models.CharField(max_length=100)
    user_address = models.TextField()
    user_phone = models.CharField(max_length=15)
    weight = models.IntegerField(verbose_name="상품 중량")


class Payment(models.Manager):
    product_names = models.CharField(max_length=50)
    price = models.IntegerField()
    count = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.IntegerField()
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)