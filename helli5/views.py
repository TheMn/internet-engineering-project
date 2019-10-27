from django.http import HttpResponse
from django.template import loader

def home_page(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))