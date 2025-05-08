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