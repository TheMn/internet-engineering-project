from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()


# Create your models here.

class Course(models.Model):
    thumbnail = models.ImageField(upload_to="courses")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher_course")
    title = models.CharField(max_length=50)
    students = models.ManyToManyField(User, related_name="students_enrolled_course")
    period = models.CharField(max_length=50)
    HW = models.FileField()
    student_count = models.IntegerField()

    class Meta:
        unique_together = (('period', 'title'),)

    def __str__(self):
        return self.title


class Homework(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deadline = models.DateTimeField()

    def get_answers(self):
        return self.answers.all()

    def __str__(self):
        return self.title


def generate_file_url(self, filename):
    url = "homeworks/%s/%s/" % (self.homework.course.id, self.homework.id)
    print(url)
    return url


class Answers(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_answer")
    upDate = models.DateTimeField(auto_now_add=True)
    HW = models.FileField(upload_to=generate_file_url)

    # def get_absolute_url(self):
    #     return reverse('', kwargs={
    #         'pk': self.pk
    #     })


class Question(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True)
    text = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ans = models.BooleanField(default=False)

    def __str__(self):
        return self.title
