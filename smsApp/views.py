from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .send_sms import SendSms
from django.shortcuts import redirect


from .forms import smsForm
from loginApp.models import User


# Create your views here.
@csrf_protect
def sms(request):
    if request.user.has_perm('send_sms'):
        if request.method == "POST":
            form = smsForm(request.POST or None)
            print('mkmk')
            if form.is_valid():
                phones = ','.join(s for s in (form.cleaned_data['field_10_student'] + form.cleaned_data['field_10_mom']) +
                                  form.cleaned_data['field_10_dad'] + form.cleaned_data['field_11_student'] +
                                  form.cleaned_data['field_11_mom'] + form.cleaned_data['field_11_dad'])
                text = form.cleaned_data['text']
                print(text, phones)
                SendSms.send_bulk(text, phones)
            return HttpResponse(200)
        context = {
            'sms_form': smsForm,
        }
        return render(request, 'sms.html', context)
    return HttpResponse('Unauthorized', status=401)
