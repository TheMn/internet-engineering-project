from django.shortcuts import render


# Create your views here.

def seminar(request):
    return render(request, 'seminar.html', {})
