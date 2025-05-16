from django.contrib.auth.models import User as AuthUser
from django import forms
from .models import User  # your custom User model


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'user_type', 'user_cover_image', 'logo',
            'address', 'city', 'postal_code',
            'bio', 'user_is_realestate'
        ]




class UsernamePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = AuthUser
        fields = ['username', 'password']






from django import forms
from django.contrib.auth.models import User  # built-in user

class UpdateLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # Proper password hashing
        if commit:
            user.save()
        return user