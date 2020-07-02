from django.db import models
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
from loginApp.models import Subscriber, Profile
from postingApp.models import PostStuff


class SliderContent(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    post = models.ForeignKey(PostStuff, related_name='post', on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to='slider-photos', blank=True, null=True)
    visible = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # اگر تیتر نداشت از تیتر پست بگیر
        if not self.title:
            if self.post:
                self.title = self.post.title
            else:
                self.title = 'دبیرستان علامه حلی ۵'
                self.visible = False
        # اگر توضیحات نداشت از پست بگیر
        if not self.description:
            if self.post:
                self.description = self.post.description
            else:
                self.description = 'وبسایت دبیرستان پسرانه ی تیزهوشان دوره دوم علامه حلی ۵ تهران (سمپاد)'
        # اگر عکس نداشت از پست بگیر
        if not self.img:
            if self.post:
                self.img = self.post.img
        super(SliderContent, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("title", "description", "post")
