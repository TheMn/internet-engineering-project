from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .send_sms import SendSms
from django.shortcuts import redirect
from helli5.decorators import has_perm


from .forms import smsForm
from loginApp.models import User


# Create your views here.
@csrf_protect
@has_perm('send_sms')
def sms(request):

    if request.method == "POST":
        form = smsForm(request.POST or None)
        if form.is_valid():
            phones = ','.join(s for s in (form.cleaned_data['field_10_student'] + form.cleaned_data['field_10_mom']) +
                              form.cleaned_data['field_10_dad'] + form.cleaned_data['field_11_student'] +
                              form.cleaned_data['field_11_mom'] + form.cleaned_data['field_11_dad'] +
                              form.cleaned_data['teacher'])
            text = form.cleaned_data['text']
            SendSms.send_bulk(text, phones)
        return HttpResponse(200)
    context = {
        'sms_form': smsForm,
    }
    return render(request, 'sms.html', context)
