from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # ROLE_TEACHER = 1
    # ROLE_STUDENT = 2
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(('email address'), unique=True,default='SOME STRING')
    # STATUS = (
    #     (1, ('Teacher')),
    #     (2, ('Student')),
    # )
    # status = models.PositiveSmallIntegerField(
    #     choices=STATUS,
    #     default=1,
    # )
    img = models.ImageField(upload_to='profile')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    REQUIRED_FIELDS = [email,user,birth_date]

    def get_first_name(self):
        return self.first_name

    # User.add_to_class("__str__", get_first_name)

    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

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


class PostStuff(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} {} {} {}'.format(self.username, self.title,self.text,self.date)

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
        return '{} {} {} {}'.format(self.author, self.text,self.cm_date,self.approved_comment)