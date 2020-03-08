from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import models as tinymce_models


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profilePic', default="/profilePic/default.png")
    phone = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=50, default='دانش آموز')
    description = tinymce_models.HTMLField()

    CHOICE = [
        ('math', 'ریاضی'),
        ('phys', 'فیزیک'),
        ('chem', 'شیمی'),
        ('bio', 'زیست'),
        ('comp', 'کامپیوتر'),
        ('eng', 'زبان'),
        ('far', 'فارسی'),
        ('other', 'سایر'),
    ]
    group = models.CharField(max_length=5, choices=CHOICE, blank=True)

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
    is_moavenO = models.BooleanField(default=False)
    is_moavenE = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_principle = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.is_student)


class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
