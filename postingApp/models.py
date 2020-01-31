from django.db import models
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
from .utils import unique_slug_generator
from loginApp.models import Subscriber, Profile
from django.core.mail import send_mail
from tinymce import models as tinymce_models
from colorfield.fields import ColorField
from jalali_date import datetime2jalali, date2jalali


class Category(models.Model):
    title = models.CharField(max_length=20)
    is_honored = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # @property
    # def get_posts(self):
    #     posts = [post for post in PostStuff.objects.all() if self in post.categories.all()]
    #     print("******* ", posts)
    #     # for mpost in PostStuff.objects.all():
    #     #     for cat in mpost.categories:
    #     #         if self == cat:
    #     #             res.append(cat)
    #     return posts


class PostStuff(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = tinymce_models.HTMLField()
    description = models.CharField(max_length=150, blank=True)
    img = models.ImageField(upload_to="thumbnails")
    date = models.DateTimeField(auto_now_add=False)
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


# @receiver(post_save, sender=PostStuff)
# def send_mail_to_subscribers(sender, instance, **kwargs):
#     send_mail(
#         instance.title,
#         instance.text,
#         'allamehelli5@ac.ir',
#         [s.email for s in Subscriber.objects.all()],
#         fail_silently=False,
#     )


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


class Event(models.Model):
    text = tinymce_models.HTMLField()
    date = models.DateField(auto_now_add=False)
    color = ColorField(default='#FF0000')

    @property
    def day_of_week(self):
        switcher = {
            '0': "شنبه",
            '1': "یکشنبه",
            '2': "دوشنبه",
            '3': "سه شنبه",
            '4': "چهارشنبه",
            '5': "پنجشنبه",
            '6': "جمعه",
        }
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", date2jalali(self.date))
        return switcher[date2jalali(self.date).strftime('%w')]
