from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.index, name='property-index'),
    path('property/<int:id>/', views.get_property_by_id, name='property-by-id'),
    path('signup/', views.signup_view, name='signup'),
    path('accounts/login/', lambda request: redirect('login')),
    path('login/', views.login_view, name='login'),
    path('property-detail/<int:id>/', views.get_property_by_id, name='property_detail'),
]