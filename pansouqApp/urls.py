from django.urls import path
from .views import *
from django.conf.urls import url, include

urlpatterns = [

    path('<pansouq_id>/', pansouq, name='pansouq'),
    # url(r'^(?P<slug>[\w-]+)/update/$', blog_update, name='blog_update'),
]
