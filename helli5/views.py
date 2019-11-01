from django.http import HttpResponse
from django.template import loader
import datetime


def home_page(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def something(request):
    now = datetime.datetime.now()
    template = loader.get_template('something.html')
    context = {'current_date': now}
    return HttpResponse(template.render(context, request))
