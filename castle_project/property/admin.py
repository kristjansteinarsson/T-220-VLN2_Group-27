from .models import Property, PropertyImage, PropertyType  # ✅ Make sure PropertyType is here
from django.contrib import admin
from .models import Property, PropertyImage  # Import your models

# Register your models
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(PropertyType)

