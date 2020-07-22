from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm, LoginForm, PreRegistrationFrom
from helli5.decorators import unauth_user
from django.contrib import messages
from .models import PreRegisteredStudent
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from paymentApp.models import Debt


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
                                     'مشخصات وارد شده در سامانه ثبت شد، برای پیگیری مراحل بعدی لازم است در بازه ی ۱۰ تا ۲۰ مرداد، ضمن به همراه داشتن ۴قطعه عکس پرسنلی و کارت واکسن ۱۵سالگی (در صورتی که تزریق واکسن در موقعیت فعلی از نظر پروتکل های بهداشتی منعی نداشته باشد)، به صورت حضوری به مدرسه مراجعه کنید.')
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
