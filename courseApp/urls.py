from django.urls import path
from .views import *

urlpatterns = [
    path('', courses, name='courses'),
    path('<int:course_id>/', course_single, name='course_single'),
    path('<int:course_id>/<int:assignment_id>/', homework, name='homework'),
    path('add_course/', add_course, name='add_course'),
]
