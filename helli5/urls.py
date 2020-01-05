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
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('djrichtextfield/', include('djrichtextfield.urls')),

    path('teacher/', views.teacher, name='teacher'),
    path('courses/', views.courses, name='courses'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('login/', views.login, name='login'),

    url(r'^postingApp/', include('postingApp.urls')),

]
