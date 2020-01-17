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


# def footer(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         new_subscriber = Subscriber()
#         new_subscriber.email = email
#         new_subscriber.save()
#     return render(request, 'footer.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def honors(request):
    return render(request, 'honors.html', {})


def about(request):
    return render(request, 'about.html', {})


def courses(request):
    return render(request, 'courses.html', {})


def teacher(request):
    return render(request, 'teacher.html', {})
