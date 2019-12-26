from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path(r'signup/', views.signup, name='signup'),
    url(r'login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # by default login will redirect user to /accounts/profile
    url(r'logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
