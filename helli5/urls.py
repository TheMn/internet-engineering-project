"""
URL Configuration for the helli5 project.

This module defines the URL patterns for the entire helli5 project. It includes
the URLs for the admin site, the different apps, and the static and media
files.
"""
from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from django.contrib import admin
from django.urls import path
from . import views
# import postingApp
import loginApp
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from postingApp.feeds import LatestPostsFeed
from loginApp.views import pre_registration
from loginApp.views import export_pre_registrations
from pansouqApp.views import students_list

handler400 = views.custom_400
handler403 = views.custom_403
handler404 = views.custom_404
handler500 = views.custom_500

urlpatterns = [

    path('', views.index, name='index'),
    path('export-pres/', export_pre_registrations, name='export-pres'),

    path('admin/', admin.site.urls),
    path('feed/rss', LatestPostsFeed(), name='posts_feed'),
    path('ارتباط-با-ما/', views.contact, name='contact'),
    path('درباره-ما/', views.about, name='about'),
    path('کنکور/', views.konkour, name='konkour'),
    path('دبیران/', views.teachers, name='teachers'),
    path('bunch_add', views.bunch_add_model, name='bunch_add'),
    # path('export', views.export, name='export'),

    path('پیش-ثبت-نام/', pre_registration, name='pre_registration'),
    path('complete/<melli>', pre_registration, name='compelete_form'),
    path('students_list/<challenge_id>/', students_list, name='pansouq_students'),
    # path('error503/', views.error503, name='error503'),
    # path('djrichtextfield/', include('djrichtextfield.urls')),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^حساب-ها/', include('loginApp.urls')),
    url(r'^نوشته-ها/', include('postingApp.urls')),
    url(r'^افتخارات/', include('honorsApp.urls')),
    url(r'panel/', include('smsApp.urls')),
    url(r'^courses/', include('courseApp.urls')),
    url(r'^آموزش-آنلاین/', include('eLearning.urls')),
    url(r'^پژوهشی/', include('pansouqApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
