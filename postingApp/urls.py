from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.index, name='index'),
    path('', blog, name='blog'),
    path('add_post/', add_post, name='add_post'),
    path('search/',search,name='search'),
    path('<id>/', blog_single, name='blog_single'),
]
