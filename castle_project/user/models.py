from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)
    user_type = models.CharField(max_length=20)
    user_cover_image = models.CharField(max_length=4096)
    logo = models.CharField(max_length=4096)
    address = models.CharField(max_length=4096)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10)
    bio = models.TextField(max_length=1000)
    user_is_realestate = models.BooleanField()

    def __str__(self):
        return self.name


