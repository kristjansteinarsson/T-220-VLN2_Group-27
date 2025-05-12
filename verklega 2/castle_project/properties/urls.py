from django.urls import path
from django.shortcuts import redirect
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('accounts/login/', lambda request: redirect('login')),
]
