from django.db import models

class Offer(models.Model):
    objects = None
    property_id = models.IntegerField()
    offer_date = models.DateField()
    offer_expiration = models.DateField()
    offer_status = models.CharField(max_length=10)
    user_id = models.IntegerField()
    offer_price = models.IntegerField()


