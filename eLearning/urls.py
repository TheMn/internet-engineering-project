from django.urls import path
from django.conf.urls import url
from eLearning import views

urlpatterns = [
    path('', views.elearning_stuff, name='elearning_stuff'),
    url(r'حضورغیاب', views.check_classes, name='check_classes'),
]
