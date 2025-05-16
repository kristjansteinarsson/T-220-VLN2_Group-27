from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import profile_view, signup_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='log_in.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', signup_view, name='register'),  # ✅ THIS IS THE FIX
    path('profile/', profile_view, name='profile'),
]