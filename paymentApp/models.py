from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Debt(models.Model):
    amount = models.IntegerField(verbose_name='مبلغ به ریال')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' '+self.user.last_name
