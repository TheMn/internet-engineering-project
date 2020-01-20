from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', courses, name='courses'),
    # path('download_zip/<int:assignment_id>/', download_zip, name='download_zip'),
    path('add_course/', add_course, name='add_course'),
    path('<int:course_id>/', course_single, name='course_single'),
    path('<int:course_id>/download_excel', download_excel, name='download_excel'),
    path('<int:course_id>/<int:assignment_id>/', homework, name='homework'),

]
