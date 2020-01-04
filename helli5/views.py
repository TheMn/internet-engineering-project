from django.template import loader
from django.http import HttpResponse
from datetime import datetime as dt
from django.shortcuts import render
from postingApp.models import PostStuff


def index(request):
    featured = PostStuff.objects.filter(featured=True)
    context = {
        'object_list': featured,
        'date': dt.now()
    }
    return render(request, 'index.html', context)


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
