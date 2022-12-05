from django.db import models
from user.models import UserModel
from product.models import Product



class Payment(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    total_price = models.TextField()

class Order(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    payment_num = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=50, blank=True)
    order_price = models.IntegerField(blank=True)
    count = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.IntegerField(verbose_name="주문 상태", default=0)
    user_name = models.CharField(max_length=100, blank=True)
    user_address = models.TextField()
    user_phone = models.CharField(max_length=15)
    weight = models.IntegerField(verbose_name="상품 중량")
    product_image = models.ImageField(upload_to='%y/%m/')
    receiver = models.TextField()

