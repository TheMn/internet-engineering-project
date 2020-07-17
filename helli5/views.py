from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from postingApp.models import PostStuff, Event
from loginApp.models import Profile, Subscriber, Contact
from django.db.models import Q
from loginApp.forms import ContactForm
from dynamicApp.models import SliderContent


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
    slider_contents = SliderContent.objects.filter(Q(visible=True)).order_by('-date')[0:6]
    latest = PostStuff.objects.order_by('-date')[0:6]
    events = Event.objects.filter(~Q(order=-1)).order_by('order')
    top_events = Event.objects.filter(order=-1)
    context = {
        'latest_posts': latest,
        'events': events,
        'top_events': top_events,
        'slider_contents': slider_contents
    }
    return render(request, 'index.html', context)


# def footer(request):
#     events = Event.objects.order_by('-date')[0:6]
#     context = {
#         'events': events,
#     }
#     return render(request, 'footer.html', context)


def contact(request):
    status = 0
    if request.method == 'POST':
        if request.POST.get('form-key') == 'ارتباط-با-ما':
            status = -1
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                try:
                    contact_obj = Contact(
                        name=contact_form.cleaned_data['name'],
                        email=contact_form.cleaned_data['email'],
                        subject=contact_form.cleaned_data['subject'],
                        body=contact_form.cleaned_data['body'])
                    contact_obj.save()
                    status = 1
                except:
                    pass

    context = {
        'contact_form': ContactForm(),
        'status': status
    }
    return render(request, 'contact.html', context)


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


def custom_400(request, exception):
    return render(request, '400.html', status=400)


def custom_403(request, exception):
    return render(request, '403.html', status=403)


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)
