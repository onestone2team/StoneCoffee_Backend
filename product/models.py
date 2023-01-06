from django.db import models
from user.models import UserModel
from django.core.validators import MinValueValidator, MaxValueValidator




class Category(models.Model):
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    content=models.TextField()
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()
    aroma_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    sweet_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    acidity_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    body_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    like=models.ManyToManyField(UserModel, related_name = 'like', blank=True, through='LikeTage')
    image=models.ImageField(upload_to='product_image')
    created_at = models.DateField(auto_now_add=True)
    recommend_product = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_name

class LikeTage(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    weight=models.IntegerField()
    count=models.IntegerField()
    price = models.IntegerField()
    product_image = models.ImageField(upload_to='cart_image')