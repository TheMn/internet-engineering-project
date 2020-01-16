from django.shortcuts import render
from .models import Honors, Category
from datetime import datetime as dt
from honorsApp import *


# Create your views here.
def period_options():
    school_start_year = 2011
    return ["دوره" + str(x - school_start_year + 1) for x in range(school_start_year, dt.now().year)]


def honors(request):
    honors_list = Honors.objects.all()
    cats_list = [cat for cat in Category.objects.all()]

    context = {
        'all_honors': honors_list,
        'all_cats': cats_list,
        'all_periods': period_options()
    }
    return render(request, 'honors.html', context)
