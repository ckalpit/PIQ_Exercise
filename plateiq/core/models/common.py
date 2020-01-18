from django.db import models


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal_code = models.IntegerField()
