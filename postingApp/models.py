from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)


class PostStuff(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    img = models.ImageField(upload_to='profile')
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text