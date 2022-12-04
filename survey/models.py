from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Survey(models.Model):
    aroma_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sweet_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    acidity_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    body_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])