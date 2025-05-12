from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name = 'property-index'),
    path('<int:id>', views.get_property_by_id, name='property-by-id'),
]