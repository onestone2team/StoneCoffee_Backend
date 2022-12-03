from django.db import models
from user.models import UserModel
from django.core.validators import MinValueValidator, MaxValueValidator




class Category(models.Model):
    type=models.CharField(max_length=50)


class Product(models.Model):
    Catagory_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    content=models.TextField()
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    aroma_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sweet_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    acidity_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    body_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    like=models.ManyToManyField(UserModel, related_name = 'like', blank=True)
    type=models.IntegerField()
    image=models.ImageField(upload_to='product_image')
