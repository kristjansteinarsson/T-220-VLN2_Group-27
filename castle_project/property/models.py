from django.db import models

from user.models import User

class PropertyType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Property(models.Model):
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
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='properties'
    )

class PropertyImage(models.Model):
    image_url = models.CharField(max_length=4096)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)