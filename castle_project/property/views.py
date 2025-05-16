from user.views import get_or_create_custom_user
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required

from property.models import Property, PropertyImage, PropertyType
from user.models import User as CustomUser
from .forms.property_create_form import PropertyCreateForm
from .forms.property_update_form import PropertyUpdateForm
from django.contrib.auth.models import AnonymousUser

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
    return render(request, "property/properties.html", {"properties": props})

def get_property_by_id(request, property_id):
    if settings.DISABLE_DB:
        props = MOCK_PROPERTY
        is_owner = False
    else:
        props = get_object_or_404(Property, id=property_id)

        # 🔐 Check if the logged-in user is the owner
        is_owner = False
        if request.user.is_authenticated:
            try:
                custom_user = CustomUser.objects.get(auth_user=request.user)
                is_owner = (props.user == custom_user)
            except CustomUser.DoesNotExist:
                pass

    return render(request, "property/property-detail.html", {
        "property": props,
        "is_owner": is_owner,
    })


def get_property_type_by_id(request):
    property_types = PropertyType.objects.all()
    return render(request, 'home.html', {'property_types': property_types})

def home(request):
    print("hello")
    if settings.DISABLE_DB:
        properties = [MOCK_PROPERTY, MOCK_PROPERTY]
        property_types = []
        min_price = 0
        max_price = 0
    else:
        property_types = PropertyType.objects.all()
        properties = Property.objects.all()

        try:
            min_price = int(request.GET.get('min_price', 0))
        except ValueError:
            min_price = 0

        try:
            max_price = int(request.GET.get('max_price', 20000000))
        except ValueError:
            max_price = 20000000

        properties = properties.filter(price__gte=min_price, price__lte=max_price)

        property_type_id = request.GET.get('property_type')
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

    print("🧪 Final queryset:", properties.query)
    print("🧪 Count:", properties.count())
    print("🛠 Properties count:", properties.count())
    print("🛠 Filters applied: min =", min_price, ", max =", max_price)
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

@login_required
def create_property(request):
    custom_user = get_or_create_custom_user(request)  # ✅ must return saved instance

    if request.method == "POST":
        form = PropertyCreateForm(request.POST)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.user = custom_user  # ✅ Must be saved and real
            print("Saving with CustomUser ID:", custom_user.id)
            prop.save()  # 💥 This will fail if custom_user is not in the DB

            image_url = form.cleaned_data.get('image')
            if image_url:
                PropertyImage.objects.create(property=prop, image_url=image_url)

            return redirect('my-properties')
    else:
        form = PropertyCreateForm()

    return render(request, "property/create_property.html", {'form': form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms.property_create_form import PropertyCreateForm
from property.models import PropertyImage  # <- this must exist

def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    # Optionally check if request.user is owner here for safety
    property.delete()
    return redirect('my-properties')

def update_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == "POST":
        form = PropertyUpdateForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property-by-id', property_id=property_id)  # 🔁 Fixed here
    else:
        return render(request, 'property/update_property.html', {
            'id': property_id,  # 🔁 Fixed here too
            'form': PropertyUpdateForm(instance=property)
        })

def offer_view(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    dummy_offer = {
        'status': 'demo',
        'price': property.price * 0.9,
        'contact_phone': '+354 123 4567',
        'contact_email': 'offers@example.com'
    }

    return render(request, 'offer.html', {
        'property': property,
        'offer': dummy_offer
    })

@login_required
def my_properties(request):
    try:
        custom_user = CustomUser.objects.get(auth_user=request.user)
    except CustomUser.DoesNotExist:
        return redirect('profile')

    properties = Property.objects.filter(user=custom_user)
    return render(request, "property/my_properties.html", {
        'properties': properties
    })
