from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from postingApp.models import PostStuff, Event
from loginApp.models import Profile, Contact
from django.db.models import Q
from loginApp.forms import ContactForm
from dynamicApp.models import SliderContent
import os
from helli5 import settings
from django.shortcuts import render, redirect
from .forms import BunchAddForm
from django.http import HttpResponse
import xlrd
import xlwt
from loginApp.models import Profile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


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
    return render(request, '401.html', status=403)


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)


def bunch_add_model(request):
    user = request.user
    if user.is_authenticated and user.username == 'admin':
        if request.method == "POST":
            form = BunchAddForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES.getlist('file')[0]
                model_type = form.cleaned_data['model_type']
                path = settings.MEDIA_ROOT + '/excels/'
                if not os.path.isdir(path):
                    os.makedirs(path)
                with open(path + '/' + file.name, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                excel_folders = path
                excel_file_path = excel_folders + file.name
                loc = (excel_file_path)
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                rows = sheet.nrows
                if model_type == 'user':
                    User = get_user_model()
                    for i in range(1, rows):
                        user = User()
                        username = sheet.cell_value(i, 0)
                        # Integers may be stored as floats in Excel
                        # This leads to having usernames with trailing zeros, like 40000000.0
                        if isinstance(username, float) and username == int(username):
                            username = int(username)
                        user.username = username
                        password = sheet.cell_value(i, 1)
                        # same problem as above
                        if isinstance(password, float) and password == int(password):
                            password = int(password)
                        user.set_password(str(password))
                        user.first_name = sheet.cell_value(i, 2)
                        user.last_name = sheet.cell_value(i, 3)
                        user.email = sheet.cell_value(i, 4)
                        group = Group.objects.get(name=sheet.cell_value(i, 5))
                        user.save()
                        user.groups.add(group)
                        user.save()
                        profile = user.profile
                        profile.user = user
                        profile.job_title = sheet.cell_value(i, 6)
                        profile.mom_number = int(sheet.cell_value(i, 7))
                        profile.dad_number = int(sheet.cell_value(i, 8))
                        profile.phone = int(sheet.cell_value(i, 9))
                        profile.save()
            context = {
                'bunch_add': BunchAddForm,
            }

            return render(request, 'bunch_add.html', context)
        context = {
            'bunch_add': BunchAddForm,
        }
        return render(request, 'bunch_add.html', context)
    return HttpResponse(401)


def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Profile.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Profile')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['user', 'phone', 'grade', 'job_title', 'mom_number', 'dad_number']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Profile.objects.all().values_list('user', 'phone', 'grade', 'job_title', 'mom_number', 'dad_number')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def konkour(request):
    return render(request, 'konkour.html')
