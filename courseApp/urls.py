from django.urls import path
from .views import *

urlpatterns = [
    path('', courses, name='courses'),
    path('course_single/', course_single, name='course_single'),
    path('add_course/', add_course, name='add_course'),
    path('homework/', homework, name='homework'),
]
