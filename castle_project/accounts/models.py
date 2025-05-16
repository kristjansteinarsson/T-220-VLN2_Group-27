from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_cover_image = models.CharField(max_length=4096, blank=True, null=True)
    logo = models.CharField(max_length=4096, blank=True, null=True)
    address = models.CharField(max_length=4096, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    user_is_realestate = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/default-avatar.png')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
