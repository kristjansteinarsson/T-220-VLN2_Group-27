from django import forms
from accounts.models import CustomUser

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'address', 'city', 'postal_code', 'bio', 'profile_image']


from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import CustomUser  # adjust if needed

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',)