from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from property.models import Property 
from user.models import User
from offer.models import Offer


def index(request):
    return render(request, "offer/offers.html", {
        'offers': [{
            'id': x.id,
            'property_id': x.property_id,
            'offer_date': x.offer_date,
            'offer_expiration': x.offer_expiration,
            'offer_status': x.offer_status,
            'user_id': x.user_id,
            'offer_price': x.offer_price

        } for x in Offer.objects.all()],
    })

def home(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, 'log_in.html')

def signup_view(request):
    return render(request, 'sign_up.html')



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