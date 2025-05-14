from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from property.models import Property, PropertyImage
from user.models import User
from .forms.property_create_form import PropertyCreateForm
from .forms.property_update_form import PropertyUpdateForm


def index(request):
    if 'search_filter' in request.GET:
        return JsonResponse({
            'data': [{
                'address': x.address,
                'price': x.price,
                'postal_code': x.postal_code,
                'image_url': x.propertyimage_set.first().image if x.propertyimage_set.exists() else None

            } for x in Property.objects.filter(address__icontains=request.GET['search_filter']).order_by('address')]
        })

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
    properties = Property.objects.all()  # Limit to top 6 for example
    return render(request, "home.html", {"properties": properties})

def login_view(request):
    return render(request, 'log_in.html')

def signup_view(request):
    return render(request, 'sign_up.html')


def create_property(request):
    if request.method == "POST":
        form = PropertyCreateForm(request.POST)
        if form.is_valid():
            property = form.save()
            property_image = form.cleaned_data.get('image')

            # Fix: Use image_url instead of image
            image = PropertyImage(image_url=property_image, property=property)
            image.save()

            return redirect('property-by-id', id=property.id)
    else:
        return render(request, "property/create_property.html", {
            'form': PropertyCreateForm()
        })

def delete_property(request, id):
    property = get_object_or_404(Property, id=id)
    property.delete()
    return redirect('property-index')


def update_property(request, id):
    property = get_object_or_404(Property, id=id)
    if request.method =="POST":
        form = PropertyUpdateForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect(f'property-by-id', id=id)
    else:
        return render(request, 'property/update_property.html', {
            'id': id,
            'form': PropertyUpdateForm(instance=property)
        })