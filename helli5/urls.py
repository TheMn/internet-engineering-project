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

urlpatterns = [

    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('teacher/', views.teacher, name='teacher'),
    path('index/', views.index, name='index'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('djrichtextfield/', include('djrichtextfield.urls')),

    url(r'^account/', include('loginApp.urls')),
    url(r'^post/', include('postingApp.urls')),

]
