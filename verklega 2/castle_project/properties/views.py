from django.shortcuts import render, redirect

# Home view
def home(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        # Regardless of what is typed, redirect to home
        return redirect('home')
    return render(request, 'log_in.html')

# Sign up view
def signup_view(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'sign_up.html')

