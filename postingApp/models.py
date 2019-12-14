from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ROLE_TEACHER = 1
    ROLE_STUDENT = 2
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(('email address'), unique=True,default='SOME STRING')
    STATUS = (
        (1, ('Teacher')),
        (2, ('Student')),
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS,
        default=1,
    )
    img = models.ImageField(upload_to='profile')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    REQUIRED_FIELDS = [email,user,birth_date]

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class PostStuff(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    def __str__(self):
        return self.username

class Attachment(models.Model):
    post = models.ForeignKey(PostStuff, on_delete=models.CASCADE)
    attach = models.FileField(upload_to='uploads/%Y/%m/%d/')


class Comment(models.Model):
    post = models.ForeignKey(PostStuff, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
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