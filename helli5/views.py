from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from postingApp.models import PostStuff
from loginApp.models import Subscriber


def index(request):
    if request.method == "POST":
        email = request.POST["email"]
        new_subscriber = Subscriber()
        new_subscriber.email = email
        new_subscriber.save()
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


def course_teacher(request):
    return render(request, 'course_teacher.html', {})


def about(request):
    return render(request, 'about.html', {})


def courses(request):
    return render(request, 'courses.html', {})


def example(request):
    return render(request, 'example.html', {})


def base(request):
    return render(request, 'base.html', {})


def error503(request):
    return render(request, 'error503.html', {})

def course_single(request):
    return render(request, 'course_single.html', {})


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
