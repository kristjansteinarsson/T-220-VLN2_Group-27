from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.models import User
from property.models import Property

def index(request):
    return render(request, "user/users.html", {
        'users': User.objects.all()
    })

def get_user_by_id(request, id):
    manu = User.objects.get(id=id)
    return render(request, "user/user-detail.html", {
        "user": manu
    })

def get_user_properties(request, id):
    manu = User.objects.get(id=id)
    print("property.id check: ",manu.properties.all())  # Check if properties are being returned

    for property in manu.properties.all():
        print(property.id)  # Check if each property has a valid ID

    return render(request, "user/user_properties.html", {
        "user": manu,
        "properties": manu.properties.all()
    })

def register(request):
    print("🔔 register called, method=", request.method)
    if request.method == "POST":
        print("🔔 received POST data:", request.POST)
        form = UserCreationForm(request.POST)
        print("🔔 form fields:", form.fields.keys())
        if form.is_valid():
            print("✅ form valid!")
            form.save()
            return redirect('login')
        print("🚨 form invalid:", form.errors)
        return render(request, 'user/sign_up.html', {'form': form})
    print("🔔 GET request – rendering form")
    return render(request, 'user/sign_up.html', {'form': UserCreationForm()})

def profile(request):
    return render(request, 'user/profile.html')