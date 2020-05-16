from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from postingApp.models import PostStuff
from loginApp.models import Profile
from postingApp.models import Event
from django.db.models import Q
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
    events = Event.objects.filter(~Q(order=-1)).order_by('order')
    top_events = Event.objects.filter(order=-1)
    context = {
        'latest_posts': latest,
        'events': events,
        'top_events': top_events,
    }
    return render(request, 'index.html', context)


# def footer(request):
#     events = Event.objects.order_by('-date')[0:6]
#     context = {
#         'events': events,
#     }
#     return render(request, 'footer.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def teachers(request):
    math_teachers = Profile.objects.filter(group='math')
    phys_teachers = Profile.objects.filter(group='phys')
    chem_teachers = Profile.objects.filter(group='chem')
    bio_teachers = Profile.objects.filter(group='bio')
    comp_teachers = Profile.objects.filter(group='comp')
    eng_teachers = Profile.objects.filter(group='eng')
    far_teachers = Profile.objects.filter(group='far')
    other_teachers = Profile.objects.filter(group='other')

    groups = {
        'ریاضی': math_teachers,
        'زیست': bio_teachers,
        'فیزیک': phys_teachers,
        'شیمی': chem_teachers,
        'کامپیوتر': comp_teachers,
        'زبان': eng_teachers,
        'فارسی': far_teachers,
        'سایر': other_teachers,
    }
    context = {
        'groups': groups
    }
    return render(request, 'teachers.html', context)

# def error503(request):
#     return render(request, 'error503.html', {})
