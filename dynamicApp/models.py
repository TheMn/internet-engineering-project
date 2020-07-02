from django.db import models
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
from loginApp.models import Subscriber, Profile
from django.core.mail import send_mail
from tinymce import models as tinymce_models
from postingApp.models import PostStuff


class SliderContent(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    post = models.ForeignKey(PostStuff, related_name='post', on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to='slider-photos', blank=True, null=True)
    visible = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_title()

    def get_post_url(self):
        return self.post.get_absolute_url() if self.post else None

    def get_title(self):
        if self.title:
            return self.title
        elif self.post:
            return self.post.title
        else:
            return None

    def get_description(self):
        if self.description:
            return self.description
        elif self.post:
            return self.post.description
        else:
            return None

    def get_img_url(self):
        if self.img:
            return self.img.url
        elif self.post:
            return self.post.img.url
        else:
            return None
