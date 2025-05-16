from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from user.models import User as CustomUser
from property.models import Property
from .forms import UserProfileForm, UpdateLoginForm

# ✅ Reusable helper function – place near the top

def get_or_create_custom_user(request):
    auth_user = request.user
    custom_user, created = CustomUser.objects.get_or_create(
        auth_user=auth_user,
        defaults={
            'name': auth_user.username,
            'user_type': '',
            'user_cover_image': '',
            'logo': '',
            'address': '',
            'city': '',
            'postal_code': '',
            'bio': '',
            'user_is_realestate': False
        }
    )
    if created:
        custom_user.save()  # 💾 Make sure it exists in the DB
    return custom_user

# Show all custom users
def index(request):
    return render(request, "user/users.html", {
        'users': CustomUser.objects.all()
    })

# Show a specific user by ID
def get_user_by_id(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, "user/user-detail.html", {"user": user})

# Show properties owned by a specific user
def get_user_properties(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, "user/user_properties.html", {
        "user": user,
        "properties": user.properties.all()
    })

# Register + create custom user profile
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth_user = form.save()
            login(request, auth_user)

            CustomUser.objects.get_or_create(auth_user=auth_user, defaults={
                'name': auth_user.username,  # 💡 Also required here
                'user_type': '',
                'user_cover_image': '',
                'logo': '',
                'address': '',
                'city': '',
                'postal_code': '',
                'bio': '',
                'user_is_realestate': False,
            })

            request.session['user_id'] = auth_user.id
            return redirect('profile')
    else:
        form = UserCreationForm()

    return render(request, 'user/sign_up.html', {'form': form})

# Profile view — handles both profile + auth updates
@login_required
def profile_view(request):
    auth_user = request.user
    custom_user = get_or_create_custom_user(request)

    form = UserProfileForm(instance=custom_user)
    auth_form = UpdateLoginForm(instance=auth_user)

    if request.method == 'POST':
        if 'profile_submit' in request.POST:
            form = UserProfileForm(request.POST, instance=custom_user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated.")
                return redirect('profile')

        elif 'auth_submit' in request.POST:
            auth_form = UpdateLoginForm(request.POST, instance=auth_user)
            if auth_form.is_valid():
                auth_form.save()
                update_session_auth_hash(request, auth_user)
                messages.success(request, "Login info updated.")
                return redirect('profile')

    return render(request, 'user/profile.html', {
        'form': form,
        'auth_form': auth_form,
        'user': custom_user,
    })

# Optional view
def update_login_info(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user

    if request.method == 'POST':
        form = UpdateLoginForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateLoginForm(instance=user)

    return render(request, 'user/update_login.html', {'form': form})
