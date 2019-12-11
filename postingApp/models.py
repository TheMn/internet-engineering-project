from django.db import models

# Create your models here.
class postStuff(models.Model):
    title = models.CharField(max_length=100)
    userName = models.CharField(max_length=50)
    text = models.CharField(max_length=400)
    img = models.ImageField(upload_to='profile')
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text