from django.db import models
from user.models import UserModel
from product.models import Product, Category

# Create your models here.
class Inquiry(models.Model):
    content = models.TextField()
    answer = models.TextField()
    status = models.BooleanField(null=True)
    title = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)