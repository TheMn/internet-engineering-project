from django.db import models
from postingApp.models import Category


# Create your models here.
class Honors(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="honors")
    categories = models.ManyToManyField(Category)
    period = models.CharField(max_length=50)
