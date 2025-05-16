from django.shortcuts import redirect
from django.urls import path
from .views import (
    home,
    index,
    get_property_by_id,
    offer_view,
    signup_view,
    login_view,
    create_property,
    update_property,
    delete_property,
    my_properties,
)

urlpatterns = [
    path('', home, name='home'),  # Main homepage
    path('properties/', index, name='property-index'),  # List all properties

    path('property/<int:property_id>/', get_property_by_id, name='property-by-id'),
    path('property/<int:property_id>/offer/', offer_view, name='offer-view'),

    path('signup/', signup_view, name='signup'),
    path('accounts/login/', lambda request: redirect('login')),  # Redirect Django default login path
    path('login/', login_view, name='login'),

    path('create/', create_property, name='create-property'),
    path('update/<int:property_id>/', update_property, name='update-property'),

    path('delete/<int:property_id>/', delete_property, name='delete-property'),

    path('my/', my_properties, name='my-properties'),
]
