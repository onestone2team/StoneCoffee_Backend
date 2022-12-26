from django.db import models
from user.models import UserModel
from product.models import Product



class Payment(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    total_price = models.TextField(blank=True, null=True)
    # 0 == 주문, 3 == 주문 취소 요청, 4 == 주문 취소
    status = models.IntegerField(default=0)


class Order(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    payment_num = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=50, blank=True)
    order_price = models.IntegerField(blank=True)
    count = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user_name = models.CharField(max_length=100, blank=True)
    user_address = models.TextField()
    user_phone = models.CharField(max_length=15)
    weight = models.IntegerField(verbose_name="상품 중량")
    product_image = models.ImageField(upload_to='%y/%m/')
    receiver = models.TextField()
    # 0 == 확인 대기, 1 == 배송중, 2 == 배송완료, 3 == 주문 취소 요청, 4 == 주문 취소
    status = models.IntegerField(verbose_name="주문 상태", default=0)

class OrderCancel(models.Model):

    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name="order_product")
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, related_name="payment_num")
    price = models.IntegerField()
    user = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, related_name="username")
    created_at = models.DateField(auto_now_add=True)
    # 3 == 주문 취소 요청, 4 == 주문 취소, 6 베달비 결제
    status = models.IntegerField(default=0)
