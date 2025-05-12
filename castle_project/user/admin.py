from django.contrib import admin

from django.contrib import admin
from .models import User  # Import your User model

admin.site.register(User)  # Register it with the admin site
