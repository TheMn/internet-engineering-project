from django.urls import path
from .views import *

urlpatterns = [
    path('', blog, name='blog'),
    path('add_post_teacher/', add_post_teacher, name='add_post_teacher'),
    path('add_post/', add_post, name='add_post'),
    path('<id>/', blog_single, name='blog_single'),
]
