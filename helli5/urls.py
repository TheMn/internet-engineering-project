"""helli5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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
    path('دبیران/', views.teachers, name='teachers'),
    path('bunch_add', views.bunch_add_model, name='bunch_add'),
    path('export', views.export, name='export'),

    # path('پیش-ثبت-نام/', pre_registration, name='pre_registration'),
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
