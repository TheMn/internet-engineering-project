from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)


class PostStuff(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    img = models.ImageField(upload_to='profile')
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey(PostStuff, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    cm_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

#this below line will allow our comment table to be related to 2 different tables
    class Meta:
        unique_together = (('post', 'author'),)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text