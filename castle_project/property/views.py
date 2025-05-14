from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from property.models import Property, PropertyImage, PropertyType
from user.models import User
from django.conf import settings
from .forms.property_create_form import PropertyCreateForm
from .forms.property_update_form import PropertyUpdateForm

MOCK_PROPERTY = {
    "propertyimage_set": None,
    "id": 1,
    "location": "HEllo",
    "description": "Desc",
    "address": "Mosabard",
    "house_number": 16,
    "city": "Hafnarfjordur",
    "user": {"id": 1}
}

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
    if settings.DISABLE_DB:
        props = MOCK_PROPERTY
    else:
        props = Property.objects.get(id=id)

    return render(request, "property/property-detail.html", {
        "property": props
    })

def get_property_type_by_id(request):
    property_types = PropertyType.objects.all()
    return render(request, 'home.html', {
        'property_types': property_types,
    })

def get_property_type_by_id(request):
    property_types = PropertyType.objects.all()
    return render(request, 'home.html', {
        'property_types': property_types,
    })

from .models import Property

from django.shortcuts import render
from .models import Property, PropertyType

def home(request):
    if settings.DISABLE_DB:
        properties = [
            MOCK_PROPERTY,
            MOCK_PROPERTY,
        ]
        property_types = []
        min_price = 0
        max_price = 0
    else:
        property_types = PropertyType.objects.all()

        properties = Property.objects.all()

        min_price = request.GET.get('min_price', 0)
        max_price = request.GET.get('max_price', 20000000)

        if min_price:
            properties = properties.filter(price__gte=min_price)
        if max_price:
            properties = properties.filter(price__lte=max_price)

        property_type_id = request.GET.get('property_type', None)
        if property_type_id:
            properties = properties.filter(property_type__id=property_type_id)

        postal_code = request.GET.get('postal_code', '').strip()
        if postal_code:
            properties = properties.filter(postal_code__icontains=postal_code)


    return render(request, "home.html", {
        'properties': properties,
        'property_types': property_types,
        'min_price': min_price,
        'max_price': max_price,
    })

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


def offer_view(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    dummy_offer = {
        'status': 'demo',
       'price': property.price * 0.9,  # 10% below asking as example
        'contact_phone': '+354 123 4567',
        'contact_email': 'offers@example.com'
    }
    
    return render(request, 'offer.html', {
        'property': property,
        'offer': dummy_offer 
    })
