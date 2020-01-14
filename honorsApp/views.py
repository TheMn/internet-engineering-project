from django.shortcuts import render
from .models import Honors


# Create your views here.

def honors(request):
    honors_list = Honors.objects.all()
    context = {
        'all_honors': honors_list
    }
    return render(request, 'honors.html', context)
