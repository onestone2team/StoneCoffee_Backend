from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import UserModel
# Create your models here.

class Survey(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True, related_name='user_survey')
    aroma_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sweet_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    acidity_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    body_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])