from django.urls import path
from django.conf.urls import url
from eLearning import views

urlpatterns = [
    url(r'check_classes', views.check_classes, name='check_classes'),
]
