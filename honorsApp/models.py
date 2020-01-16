from django.db import models
from postingApp.models import Category
from datetime import datetime as dt


def period_choices():
    school_start_year = 2011
    periods = ["دوره" + str(x - school_start_year + 1) for x in range(school_start_year, dt.now().year)]
    return [x for x in zip(periods, periods)]


# Create your models here.
class Honors(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to="honors")
    categories = models.ManyToManyField(Category, limit_choices_to={'is_honored': True})
    period = models.CharField(max_length=50, choices=period_choices())

    def __str__(self):
        return self.name

    @property
    def get_class(self):
        category = " ".join([cat.title for cat in self.categories.all()])
        return " ".join([self.period, category])
