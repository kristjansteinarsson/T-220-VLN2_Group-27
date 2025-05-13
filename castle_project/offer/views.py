from django.http import HttpResponse
from django.shortcuts import render

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
