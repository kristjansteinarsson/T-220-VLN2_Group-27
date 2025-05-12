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
    return render(request, 'home.html')