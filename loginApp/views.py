from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm, LoginForm, PreRegistrationFrom
from helli5.decorators import unauth_user
from django.contrib import messages


@csrf_protect
# @unauth_user
def pre_registration(request):
    if request.method == 'POST':
        form = PreRegistrationFrom(request.POST)
        if form.is_valid():
            # form.cleaned_data['is_valid'] = True;
            form.save()
            messages.success(request,
                             'مشخصات وارد شده در سامانه ثبت شد، برای پیگیری مراحل بعدی لازم است به صورت حضوری به مدرسه مراجعه کنید')
        else:
            messages.warning(request, 'متاسفانه اطلاعات وارد شده معتبر نبوده و در سامانه ثبت نشد')
    context = {
        'pre_registration_form': PreRegistrationFrom()
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
                    return redirect('index')

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
