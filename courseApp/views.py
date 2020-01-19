from django.shortcuts import render


def courses(request):
    return render(request, 'courses.html', {})


def add_course(request):
    return render(request, 'add_course.html', {})


def course_single(request):
    return render(request, 'course_single.html', {})


def homework(request):
    return render(request, 'homework.html', {})
