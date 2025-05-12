from django.urls import path
from django.shortcuts import redirect
from . import views 

urlpatterns = [
    path('', views.login_view, name='login'), 
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),  
    path('accounts/login/', lambda request: redirect('login')),
]