from django.urls import path
from .views import *
from django.conf.urls import url, include

urlpatterns = [

    path('', blog, name='blog'),
    path('تگ/<tag>', blog, name='blog'),
    # path('add_post_teacher/', add_post_teacher, name='add_post_teacher'),
    # path('add_post/', add_post, name='add_post'),
    path('جستجو/', search, name='search'),
    # path('tag_res/<id>/', posts_by_cat, name='tag_res'),
    url(r'^(?P<slug>[\w-]+)/$', blog_single, name='blog_single'),
    # url(r'^(?P<slug>[\w-]+)/update/$', blog_update, name='blog_update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', blog_delete, name='blog_delete'),
]
