from django.http import HttpResponse
from django.shortcuts import redirect


def unauth_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def has_perm(perm):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.has_perm(perm):
                return view_func(request, *args, **kwargs)
            return HttpResponse('401 un authorized');

        return wrapper_func

    return decorator
