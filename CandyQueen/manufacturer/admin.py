from django.contrib import admin

from django.contrib import admin
from .models import Manufacturer  # Import your Manufacturer model

admin.site.register(Manufacturer)  # Register it with the admin site
