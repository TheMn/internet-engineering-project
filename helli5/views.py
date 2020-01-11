from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from postingApp.models import PostStuff


def index(request):
    latest = PostStuff.objects.order_by('-date')[0:3]
    context = {
        'latest_posts': latest
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def honors(request):
    return render(request, 'honors.html', {})


def about(request):
    return render(request, 'about.html', {})


def courses(request):
    return render(request, 'courses.html', {})


def example(request):
    return render(request, 'example.html', {})


def base(request):
    return render(request, 'base.html', {})


def teacher(request):
    return render(request, 'teacher.html', {})


def login(request):
    return render(request, 'login.html', {})

# def home(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
#
# def home(request):
#
#     template = loader.get_template('index.html')
#
#     return HttpResponse(template.render(request, {}))
