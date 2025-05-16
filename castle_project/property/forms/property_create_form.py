from django.forms import ModelForm
from django import forms
from property.models import Property, PropertyType
from property.models import Property
from property.models import PropertyType
from user.models import User

class PropertyCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    property_type = forms.ModelChoiceField(
        queryset=PropertyType.objects.all(),
        widget=forms.Select(attrs={'class': "form-control"})
    )

    class Meta:
        model = Property
        exclude = ['id', 'user']
        widgets = {
            'address': forms.TextInput(attrs={'class': "form-control"}),
            'city': forms.TextInput(attrs={'class': "form-control"}),
            'house_number': forms.TextInput(attrs={'class': "form-control"}),
            'postal_code': forms.TextInput(attrs={'class': "form-control"}),
            'price': forms.NumberInput(attrs={'class': "form-control"}),
            'nr_of_bedrooms': forms.NumberInput(attrs={'class': "form-control"}),
            'nr_of_bathrooms': forms.NumberInput(attrs={'class': "form-control"}),
            'square_meters': forms.NumberInput(attrs={'class': "form-control"}),
        }
