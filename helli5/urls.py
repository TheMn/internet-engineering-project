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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views
# import postingApp
import loginApp
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

  path('', views.index, name='index'),
  path('admin/', admin.site.urls),
  path('course_teacher/', views.course_teacher, name='course_teacher'),
  path('error503/', views.error503, name='error503'),
  path('contact/', views.contact, name='contact'),
  path('course_single/', views.course_single, name='course_single'),
  path('add_post_teacher/', views.add_post_teacher, name='add_post_teacher'),
  path('add_course/', views.add_course, name='add_course'),
  path('homework/', views.homework, name='homework'),
  path('about/', views.about, name='about'),
  path('courses/', views.courses, name='courses'),
  path('djrichtextfield/', include('djrichtextfield.urls')),

  url(r'^accounts/', include('loginApp.urls')),
  url(r'^blog/', include('postingApp.urls')),
  url(r'honors/', include('honorsApp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
