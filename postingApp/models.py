from django.db import models
from djrichtextfield.models import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profilePic')
    phone = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Role(models.Model):
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_consulter = models.BooleanField(default=False)
    is_moavenP = models.BooleanField(default=False)
    is_moavenA = models.BooleanField(default=False)
    is_moavenE = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_principle = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.is_student, self.is_teacher, self.is_consulter, self.is_moavenP,
                                                self.is_moavenA, self.is_moavenE, self.is_principle, self.is_parent)

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)


class PostStuff(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = RichTextField()
    img = models.ImageField(upload_to='profile')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.username, self.title, self.text, self.date)


class Attachment(models.Model):
    post = models.ForeignKey(PostStuff, on_delete=models.CASCADE)
    attach = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Comment(models.Model):
    post = models.ForeignKey(PostStuff, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    cm_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('post', 'author'),)
