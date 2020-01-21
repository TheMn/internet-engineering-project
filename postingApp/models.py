from django.db import models
from djrichtextfield.models import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.urls import reverse
from .utils import unique_slug_generator
from courseApp.models import Homework

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profilePic', default="/profilePic/default.png")
    phone = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Role(models.Model):
    person = models.OneToOneField(Profile, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_consulter = models.BooleanField(default=False)
    is_moavenP = models.BooleanField(default=False)
    is_moavenA = models.BooleanField(default=False)
    is_moavenE = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_principle = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.is_student)


class Category(models.Model):
    title = models.CharField(max_length=20)
    is_honored = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class PostStuff(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = RichTextField()
    description = models.CharField(max_length=150, blank=True)
    img = models.ImageField(upload_to="thumbnails")
    date = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_single', kwargs={
            'slug': self.slug
        })

    def get_update_url(self):
        return reverse('blog_update', kwargs={
            'slug': self.slug
        })

    def get_delete_url(self):
        return reverse('blog_delete', kwargs={
            'slug': self.slug
        })

    @property
    def get_comments(self):
        return self.comments.all()

    def comment_count(self):
        return Comment.objects.filter(post=self).count()


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_receiver, sender=PostStuff)


class Attachment(models.Model):
    post = models.ForeignKey(PostStuff, on_delete=models.CASCADE)
    attach = models.FileField(upload_to='uploads/%Y/%m/%d/')


class Comment(models.Model):
    post = models.ForeignKey(PostStuff, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    cm_date = models.DateTimeField(auto_now_add=True)
