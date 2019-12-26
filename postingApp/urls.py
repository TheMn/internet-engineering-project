from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.make_post, name='get_post'),

]
