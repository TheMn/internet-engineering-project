from django.urls import path
from .views import *

urlpatterns = [
    path('', honors, name='honors'),
]
