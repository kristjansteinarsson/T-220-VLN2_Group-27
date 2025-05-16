from django.urls import path

from . import views
from .views import offer_view

urlpatterns = [
    path('', views.index , name = 'offer-index'),
    path('property/<int:property_id>/offer/', offer_view, name='property-offer')
]