from django.template import loader
from django.http import HttpResponse
from datetime import datetime as dt
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


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    # featured = PostStuff.objects.filter(featured=True)
    # context = {
    #     'featured_posts': featured,
    # }
    return render(request, 'blog.html', {})


# TODO: Define these:

def courses(request):
    return render(request, 'courses.html', {})


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
