from django.db import models

class Manufacturer(models.Model):
    objects = None
    name = models.CharField(max_length=40)
    user_type = models.CharField(max_length=20)
    manufacturer_cover_image = models.CharField(max_length=4096)
    logo = models.CharField(max_length=4096)
    address = models.CharField(max_length=4096)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10)
    bio = models.TextField(max_length=1000)


