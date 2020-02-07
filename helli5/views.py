from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from postingApp.models import PostStuff
from loginApp.models import Subscriber


def index(request):
    # TODO: uncomment subscribe form
    # if request.method == "POST":
    #     if request.POST.get('submit') == 'عضویت':
    #         try:
    #             email = request.POST["email"]
    #             new_subscriber = Subscriber()
    #             new_subscriber.email = email
    #             new_subscriber.save()
    #         except Exception:
    #             pass
    latest = PostStuff.objects.order_by('-date')[0:3]
    context = {
        'latest_posts': latest
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def teachers(request):
    return render(request, 'teachers.html', {})


# def error503(request):
#     return render(request, 'error503.html', {})


