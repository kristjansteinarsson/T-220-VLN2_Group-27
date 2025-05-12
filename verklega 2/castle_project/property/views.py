from django.shortcuts import render, redirect

# Home view
def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'log_in.html')

def signup_view(request):
    return render(request, 'sign_up.html')