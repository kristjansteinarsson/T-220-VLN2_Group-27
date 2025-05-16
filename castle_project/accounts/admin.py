from django.contrib import admin
from .models import CustomUser  # or whatever your user model is called

admin.site.register(CustomUser)
