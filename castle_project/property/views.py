from django.http import HttpResponse
from django.shortcuts import render
from property.models import Property
def index(request):
    props = Property.objects.all()
    return render(request, "property/properties.html", {
        "properties": props,
    })

def get_property_by_id(request, id):
    props = Property.objects.get(id=id)
    return render(request, "property/property-detail.html", {
        "property": props
    })

from .models import Property

def home(request):
    properties = Property.objects.all()[:6]  # Limit to top 6 for example
    return render(request, "home.html", {"properties": properties})

def login_view(request):
    return render(request, 'log_in.html')

def signup_view(request):
    return render(request, 'sign_up.html')

