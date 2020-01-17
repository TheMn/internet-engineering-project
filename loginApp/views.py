from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm


@csrf_protect
def login(request):
    login_form, signup_form = None, None
    if request.method == "POST":
        if request.POST.get('submit') == 'ورود':
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('index')
        elif request.POST.get('submit') == 'ثبت نام':
            pass
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.birth_date = form.cleaned_data.get('birth_date')
                user.profile.phone = form.cleaned_data.get('phone')
                # user.profile.img = request.POST['img']
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                print(user)
                auth_login(request, user)
                return redirect('index')
    return render(request, 'login.html', {'form': signup_form})
