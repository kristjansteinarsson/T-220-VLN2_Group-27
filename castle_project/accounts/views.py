from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms.forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

from accounts.forms.forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'sign_up.html', {'form': form})


#def login_view(request):
#    if request.user.is_authenticated:
#        print("User already logged in. Redirecting to home.")
#        return redirect('profile')
#
#    if request.method == 'POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            print("Login successful")
#            return redirect('profile')
#        else:
#            print("Login failed")
#            return render(request, 'log_in.html', {'error': 'Invalid credentials'})
#
#    return render(request, 'log_in.html')
