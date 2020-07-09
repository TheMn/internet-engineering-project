from django.urls import path
from .views import *
from django.conf.urls import url, include

urlpatterns = [
    path('sms', sms, name='sms'),

]
