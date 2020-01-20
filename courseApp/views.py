from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from .utils import create_zip

import csv
from django.http import HttpResponse
from django.contrib.auth.models import User


# def download_zip(request, assignment_id):
#     this_assignment = Homework.objects.get(id=assignment_id)
#     files = []
#     answers = Answers.objects.all()
#     for ans in answers:
#         if assignment_id == ans.homework.id:
#             files.append(ans.HW.url)
#             print("********** ", ans.HW.url)
#     print(create_zip(this_assignment, files))

def download_excel(request, course_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])
    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)
    return response


def courses(request):
    course_list = Course.objects.all()
    context = {
        'course_list': course_list
    }
    return render(request, 'courses.html', context)


def add_course(request):
    return render(request, 'add_course.html', {})


def course_single(request, course_id):
    this_course = get_object_or_404(Course, id=course_id)
    context = {
        'this_course': this_course
    }
    return render(request, 'course_single.html', context)


def homework(request, course_id, assignment_id):
    related_course = get_object_or_404(Course, id=course_id)
    this_assignment = get_object_or_404(Homework, id=assignment_id, course=related_course)
    context = {
        'this_assignment': this_assignment
    }
    return render(request, 'homework.html', context)
