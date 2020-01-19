from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *


def courses(request):
    return render(request, 'courses.html', {})


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
