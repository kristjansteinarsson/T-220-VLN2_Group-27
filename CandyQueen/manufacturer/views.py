from django.http import HttpResponse
from django.shortcuts import render

from manufacturer.models import Manufacturer

def index(request):
    return render(request, "manufacturer/manufacturers.html", {
        'manufacturers': [{
            'id': x.id,
            'name': x.name,
            'user_type': x.user_type,
            'manufacturer_cover_image': x.manufacturer_cover_image,
            'logo': x.logo,
            'address': x.address,
            'city': x.city,
            'postal_code': x.postal_code,
            'bio': x.bio

        } for x in Manufacturer.objects.all()],
    })
