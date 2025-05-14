from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name = 'user-index'),
    path('<int:id>', views.get_user_by_id, name='user-by-id'),
    path('<int:id>/properties/', views.get_user_properties, name='user_properties'),
    # Option A: register under /user/register/
    path('register/', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/log_in.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='property-index'), name='logout'),
    path('profile', views.profile, name='profile'),

]