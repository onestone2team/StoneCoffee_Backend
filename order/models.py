from django.db import models
from user.models import UserModel
from product.models import Product
from survey.models import Survey


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    order_price = models.IntegerField()
    count = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField()