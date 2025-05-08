from django.db import models

from manufacturer.models import Manufacturer

class PropertyType(models.Model):
    name = models.CharField(max_length=30)

class Property(models.Model):
    objects = None
    address = models.TextField()
    house_number = models.IntegerField()
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10)
    price = models.IntegerField()
    nr_of_bedrooms = models.IntegerField()
    nr_of_bathrooms = models.IntegerField()
    square_meters = models.IntegerField()
    sold = models.BooleanField()
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class PropertyImage(models.Model):
    image_url = models.CharField(max_length=4096)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)