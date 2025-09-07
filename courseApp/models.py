"""
Models for the course app.

This module contains the models for the course app, which handles courses,
homework, answers, questions, and reports.
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from .utils import create_zip

# from honorsApp.models import period_choices

User = get_user_model()


class Course(models.Model):
    """
    Represents a course in the eLearning platform.

    Attributes:
        thumbnail (ImageField): A thumbnail image for the course.
        teacher (ForeignKey): The user who teaches the course.
        title (CharField): The title of the course.
        students (ManyToManyField): The students enrolled in the course.
        period (CharField): The academic period during which the course is offered.
        student_count (IntegerField): The number of students in the course.
    """
    thumbnail = models.ImageField(upload_to="courses")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher_course")
    title = models.CharField(max_length=50)
    students = models.ManyToManyField(User, related_name="students_enrolled_course")
    period = models.CharField(max_length=50)
    student_count = models.IntegerField()

    class Meta:
        unique_together = (('period', 'title'),)

    def get_absolute_url(self):
        """
        Returns the absolute URL for a course instance.

        Returns:
            str: The absolute URL for the course.
        """
        return reverse('course_single', kwargs={
            'course_id': self.id
        })

    def __str__(self):
        return self.title


class Homework(models.Model):
    """
    Represents a homework assignment for a course.

    Attributes:
        title (CharField): The title of the homework.
        text (TextField): The description of the homework.
        course (ForeignKey): The course to which the homework belongs.
        created_at (DateTimeField): The date and time when the homework was created.
        deadline (DateTimeField): The deadline for submitting the homework.
    """
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='homeworks')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    @property
    def get_answers(self):
        """
        Gets all answers submitted for this homework.

        Returns:
            QuerySet: A queryset of all answers for this homework.
        """
        return self.answers.all()

    @property
    def get_questions(self):
        """
        Gets all questions related to this homework.

        Returns:
            QuerySet: A queryset of all questions for this homework.
        """
        return self.questions.all()

    # def download_all(self):
    #     zip_file = create_zip(self, self.get_answers)
    #     return zip_file

    def __str__(self):
        return self.title


def generate_file_url(self, filename):
    """
    Generates a file path for uploaded homework answers.

    Args:
        self: The instance of the model.
        filename (str): The name of the file.

    Returns:
        str: The generated file path.
    """
    url = '/'.join(['homeworks', str(self.homework.course.id), str(self.homework.id), filename])
    return url


class Answers(models.Model):
    """
    Represents a student's answer to a homework assignment.

    Attributes:
        homework (ForeignKey): The homework to which this answer belongs.
        student (ForeignKey): The student who submitted the answer.
        upDate (DateTimeField): The date and time when the answer was submitted.
        HW (FileField): The file containing the student's answer.
    """
    homework = models.ForeignKey(Homework, related_name="answers", on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_answer")
    upDate = models.DateTimeField(auto_now_add=True)
    HW = models.FileField(upload_to=generate_file_url)

    def get_files(self):
        """
        Gets a list of all answer files.

        Returns:
            list: A list of all answer files.
        """
        files_list = []
        for ans in self.objects.all():
            files_list.append(ans.HW)
        return files_list
    # def get_absolute_url(self):
    #     return reverse('', kwargs={
    #         'pk': self.pk
    #     })


class Question(models.Model):
    """
    Represents a question related to a homework assignment.

    Attributes:
        homework (ForeignKey): The homework to which this question belongs.
        title (CharField): The title of the question.
        text (TextField): The text of the question.
        date (DateField): The date when the question was asked.
        author (ForeignKey): The user who asked the question.
        ans (BooleanField): Whether the question has been answered.
    """
    homework = models.ForeignKey(Homework, related_name="questions", on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True)
    text = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ans = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Reports(models.Model):
    """
    Represents a type of report.

    Attributes:
        title (CharField): The title of the report.
    """
    title = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.title


class StudentReports(models.Model):
    """
    Represents a specific report for a student.

    Attributes:
        student (CharField): The ID of the student.
        report_url (CharField): The URL of the report file.
        report (ForeignKey): The type of report.
    """
    student = models.CharField(max_length=8, blank=False)
    report_url = models.CharField(max_length=128, blank=False)
    report = models.ForeignKey(Reports, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("add_reports", "can add reports"),
            ("see_reports", "see_reports")
        )
