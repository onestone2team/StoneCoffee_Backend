from django.db import models
from user.models import UserModel
from product.models import Product
# Create your models here.
class Inquiry(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    status = models.BooleanField(default=False)
    answer = models.TextField(null=True, blank=True)
    category = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    #type 제거 후 category 자체가 문의 종류 답변에 대해