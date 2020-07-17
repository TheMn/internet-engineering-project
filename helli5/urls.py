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
from django.conf.urls import url, include, handler404
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

# handler404 = views.custom_404

urlpatterns = [

  path('', views.index, name='index'),
  path('404/', views.custom_404, name='404'),
  path('admin/', admin.site.urls),
  path('feed/rss', LatestPostsFeed(), name='posts_feed'),
  path('ارتباط-با-ما/', views.contact, name='contact'),
  path('درباره-ما/', views.about, name='about'),
  path('دبیران/', views.teachers, name='teachers'),

  # path('error503/', views.error503, name='error503'),
  # path('djrichtextfield/', include('djrichtextfield.urls')),
  url(r'^tinymce/', include('tinymce.urls')),

  url(r'^حساب-ها/', include('loginApp.urls')),
  url(r'^نوشته-ها/', include('postingApp.urls')),
  url(r'^افتخارات/', include('honorsApp.urls')),
  url(r'panel/', include('smsApp.urls')),
  url(r'^courses/', include('courseApp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
