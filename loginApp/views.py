from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm, LoginForm, PreRegistrationFrom
from helli5.decorators import unauth_user
from django.contrib import messages
import xlwt
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from paymentApp.models import Debt
from django.http import HttpResponse
from .models import PreRegisteredStudent


@login_required(login_url='login')
def profile(request):
    user = request.user
    try:
        debt = Debt.objects.get(user=user.id)
        url = 'https://idpay.ir/allamehelli5?amount=' + str(debt.amount)
    except:
        url = None

    context = {
        "payment_url": url
    }
    return render(request, 'profile.html', context)


@csrf_protect
@unauth_user
def pre_registration(request, melli=None):
    url = None
    form = PreRegistrationFrom()
    if melli is not None:
        form = PreRegistrationFrom(instance=PreRegisteredStudent.objects.get(melli_code=melli))
    elif request.method == 'POST':
        form = PreRegistrationFrom(request.POST)
        if form.is_valid():
            valid = False
            if request.POST.get('submit') == 'final_registration':
                valid = True
            try:
                PreRegisteredStudent.objects.get(melli_code=form.cleaned_data['melli_code']).delete()
            except ObjectDoesNotExist:
                pass
            finally:
                obj = form.save(commit=False)
                obj.is_valid = valid
                obj.save()
                if valid:
                    messages.success(request,
                                     'مشخصات وارد شده در سامانه ثبت شد، برای پیگیری مراحل بعدی لازم است از شنبه ۱۷ ام مرداد، ضمن به همراه داشتن ۴قطعه عکس پرسنلی و کارت واکسن ۱۵سالگی (در صورتی که تزریق واکسن در موقعیت فعلی از نظر پروتکل های بهداشتی منعی نداشته باشد)، به صورت حضوری به مدرسه مراجعه کنید.')
                else:
                    url = "http://allamehelli5.ir/complete/" + form.cleaned_data['melli_code']
                    messages.warning(request,
                                     'اطلاعات شما موقتا در سیستم ثبت گردید،‌ برای تکمبل اطلاعات و ثبت نهایی حتما باید از طریق لینک زیر اقدام فرمایید:')
        else:
            messages.warning(request, 'متاسفانه اطلاعات وارد شده معتبر نبوده و در سامانه ثبت نشد')
    context = {
        'pre_registration_form': form,
        'complete_url': url
    }
    return render(request, 'pre_registeration.html', context)


@csrf_protect
@unauth_user
def login(request):
    login_form, signup_form = None, None
    if request.method == "POST":

        if request.POST.get('submit') == 'ورود':
            login_form = LoginForm(request.POST or None)
            if login_form.is_valid():
                user = login_form.login(request)
                if user:
                    auth_login(request, user)
                    return redirect('profile')

        elif request.POST.get('submit') == 'ثبت نام':
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.birth_date = signup_form.cleaned_data.get('birth_date')
                user.profile.phone = signup_form.cleaned_data.get('phone')
                # user.profile.img = request.POST['img']
                user.save()
                raw_password = signup_form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                print(user)
                auth_login(request, user)
                return redirect('index')

    context = {
        'login_form': login_form,
        'signup_form': signup_form
    }
    return render(request, 'login.html', context)


def export_pre_registrations(request):
    user = request.user
    if user.is_authenticated and user.username == 'admin':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['نام', 'نام خانوادگی', 'عکس پرسنلی دانش آموز', 'شماره شناسنامه', 'سریال ۶رقمی شناسنامه',
                   'سری عددی شناسنامه', 'سری حروفی شناسنامه', 'محل صدور', 'کد ملی', 'روز تولد',
                   'ماه تولد', 'سال تولد', 'شهرستان محل تولد', 'استان محل تولد', 'شهر یا روستای محل تولد', 'دین',
                   'ملیت',
                   'وضعیت جسمانی', 'چپ دست هستید؟', 'نام پدر', 'تحصیلات پدر', 'شغل پدر', 'آدرس محل کار پدر',
                   'تلفن محل کار پدر', 'تحصیلات مادر', 'شغل مادر', 'آدرس محل کار مادر', 'تلفن محل کار مادر',
                   'آدرس منزل',
                   'تلفن منزل', 'وضعیت مسکن خانواده', 'ایمیل پدر', 'شماره موبایل پدر', 'ایمیل مادر',
                   'شماره موبایل مادر',
                   'در خانواده با چه کسانی زندگی می کنید؟',
                   'وضعیت مسکن دانش آموز در صورتی که برای تحصیل دور از خانواده زندگی می کند، چگونه است؟',
                   'چندمین فرزند خانواده هستید؟', 'تعداد اعضای خانواده', 'دانش آموز اتاق مستقل برای مطالعه دارد؟',
                   'ایمیل دانش آموز', 'شماره موبایل دانش آموز', 'وضعیت تحصیلی سال قبل',
                   'رشته ی تحصیلی مورد علاقه', 'زمینه ی مورد علاقه در المپیاد های علمی',
                   'زمینه ی مورد علاقه برای فعالیت های پژوهشی', 'اگر در درسی از دروس پایه ضعف خاصی دارید، ذکر کنید',
                   'معدل کل پایه نهم', 'نام مدرسه ی قبلی', 'کد و نام مدرسه ی قبلی از روی کارنامه ی رایانه ای ثبت شود',
                   'ویژه ی ثبت نام شاهد', 'ویژه ی ثبت نام استثنایی',
                   'اگر ملاحظات خاصی وجود دارد که باید به اطلاع مدرسه و مشاورین برسد، ذکر کنید',
                   ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = PreRegisteredStudent.objects.all()
        for row in rows:
            row_num += 1
            try:
                addr = row.student_picture.url
            except:
                addr = ''
            ws.write(row_num, 0, row.student_first_name, font_style)
            ws.write(row_num, 1, row.student_last_name, font_style)
            ws.write(row_num, 2, addr, font_style)
            ws.write(row_num, 3, row.ss, font_style)
            ws.write(row_num, 4, row.ss_id, font_style)
            ws.write(row_num, 5, row.ss_numerical, font_style)
            ws.write(row_num, 6, row.ss_alphabetical, font_style)
            ws.write(row_num, 7, row.export_place, font_style)
            ws.write(row_num, 8, row.melli_code, font_style)
            ws.write(row_num, 9, row.birth_day, font_style)
            ws.write(row_num, 10, row.birth_month, font_style)
            ws.write(row_num, 11, row.birth_year, font_style)
            ws.write(row_num, 12, row.birth_place_state, font_style)
            ws.write(row_num, 13, row.birth_place_town, font_style)
            ws.write(row_num, 14, row.birth_place_city, font_style)
            ws.write(row_num, 15, row.religion, font_style)
            ws.write(row_num, 16, row.nationality, font_style)
            ws.write(row_num, 17, row.physical_situation, font_style)
            ws.write(row_num, 18, row.left_handed, font_style)
            ws.write(row_num, 19, row.father_first_name, font_style)
            ws.write(row_num, 20, row.father_edu, font_style)
            ws.write(row_num, 21, row.father_job, font_style)
            ws.write(row_num, 22, row.father_job_place, font_style)
            ws.write(row_num, 23, row.father_job_phone, font_style)
            ws.write(row_num, 24, row.mother_edu, font_style)
            ws.write(row_num, 25, row.mother_job, font_style)
            ws.write(row_num, 26, row.mother_job_place, font_style)
            ws.write(row_num, 27, row.mother_job_phone, font_style)
            ws.write(row_num, 28, row.home_location, font_style)
            ws.write(row_num, 29, row.home_phone, font_style)
            ws.write(row_num, 30, row.home_situation, font_style)
            ws.write(row_num, 31, row.father_mail, font_style)
            ws.write(row_num, 32, row.father_phone, font_style)
            ws.write(row_num, 33, row.mother_mail, font_style)
            ws.write(row_num, 34, row.mother_phone, font_style)
            ws.write(row_num, 35, row.homemate, font_style)
            ws.write(row_num, 36, row.student_own_place, font_style)
            ws.write(row_num, 37, row.this_child_counter, font_style)
            ws.write(row_num, 38, row.family_members_counter, font_style)
            ws.write(row_num, 39, row.student_have_reading_room, font_style)
            ws.write(row_num, 40, row.student_mail, font_style)
            ws.write(row_num, 41, row.student_phone, font_style)
            ws.write(row_num, 42, row.last_year_edu, font_style)
            ws.write(row_num, 43, row.field_of_study, font_style)
            ws.write(row_num, 44, row.field_of_olympiad, font_style)
            ws.write(row_num, 45, row.field_of_pajohesh, font_style)
            ws.write(row_num, 46, row.field_of_weakness, font_style)
            ws.write(row_num, 47, row.grade_at_9th, font_style)
            ws.write(row_num, 48, row.last_year_school_name, font_style)
            ws.write(row_num, 49, row.last_year_school_code, font_style)
            ws.write(row_num, 50, row.shahed_in_all_schools, font_style)
            ws.write(row_num, 51, row.exceptional_student, font_style)
            ws.write(row_num, 52, row.extra_note, font_style)

        wb.save(response)
        return response
    template = loader.get_template('401.html')
    return HttpResponse(template.render({}, request))
