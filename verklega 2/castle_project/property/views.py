from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'log_in.html')

def signup_view(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'sign_up.html')

def home(request):
    context = {
        "properties": [
            {
                "title": "Downtown Luxury Apartment",
                "image": "property1.jpeg",
                "description": "Beautiful 2-bedroom apartment with ocean views in the heart of Reykjavík.",
                "price": 8500000,
                "type" : "Apartment",
                "location": "Reykjavík 101",
            },
            {
                "title": "Cozy Suburban House",
                "image": "property2.jpeg",
                "description": "3-bedroom family home with large garden and garage.",
                "price": 12000000,
                "type" : "House",
                "location": "Kópavogur 200",
            },
            {
                "title": "Modern Harbor Condo",
                "image": "property3.jpeg",
                "description": "Stylish 1-bedroom condo with modern amenities near the old harbor.",
                "price": 6750000,
                "type" : "Condo",
                "location": "Reykjavík 105",
            },
    ]
    }
    return render(request, 'home.html', context)