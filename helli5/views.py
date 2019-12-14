from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def courses(request):
    return render(request, 'courses.html', {})

def example(request):
    return render(request, 'example.html', {})


def base(request):
    return render(request, 'base.html', {})


def teacher(request):
    return render(request, 'teacher.html', {})


def blog_single(request):
    return render(request, 'blog-single.html', {})


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