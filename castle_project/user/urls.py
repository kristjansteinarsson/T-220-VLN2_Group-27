from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name = 'user-index'),
    path('<int:id>', views.get_user_by_id, name='user-by-id'),
    path('<int:id>/properties/', views.get_user_properties, name='user_properties'),
]