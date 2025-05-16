from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(models.Model):
    auth_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, blank=True)
    user_cover_image = models.CharField(max_length=4096, blank=True)
    logo = models.CharField(max_length=4096, blank=True)
    address = models.CharField(max_length=4096, blank=True)
    city = models.CharField(max_length=30, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    user_is_realestate = models.BooleanField(default=False)

    def __str__(self):
        return self.auth_user.username
