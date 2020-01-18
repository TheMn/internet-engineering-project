from django.db import models
from django.contrib.auth import get_user_model

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




class Homework(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deadline = models.DateTimeField()


class Answers(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE,related_name="student_answer")
    upDate = models.DateTimeField(auto_now_add=True)
    HW = models.FileField()

