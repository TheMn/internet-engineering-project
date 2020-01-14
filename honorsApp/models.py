from django.db import models
from postingApp.models import Category


# Create your models here.
class Honors(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to="honors")
    categories = models.ManyToManyField(Category)
    period = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def get_class(self):
        category = " ".join([cat.title for cat in self.categories.all()])
        return ''.join(["element-item col-md-6 col-lg-4 ", category])
