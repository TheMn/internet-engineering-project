from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from postingApp.models import PostStuff
from loginApp.models import Subscriber


def index(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'عضویت':
            try:
                email = request.POST["email"]
                new_subscriber = Subscriber()
                new_subscriber.email = email
                new_subscriber.save()
            except Exception:
                pass
    latest = PostStuff.objects.order_by('-date')[0:3]
    context = {
        'latest_posts': latest
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def honors(request):
    return render(request, 'honors.html', {})


def course_teacher(request):
    return render(request, 'course_teacher.html', {})


def about(request):
    return render(request, 'about.html', {})


def courses(request):
    return render(request, 'courses.html', {})


def add_homework(request):
    return render(request, 'add_homework.html', {})


def error503(request):
    return render(request, 'error503.html', {})


def course_single(request):
    return render(request, 'course_single.html', {})


def add_course(request):
    return render(request, 'add_course.html', {})


def homework(request):
    return render(request, 'homework.html', {})


def add_post_teacher(request):
    return render(request, 'add_post_teacher.html', {})


def login(request):
    return render(request, 'login.html', {})
