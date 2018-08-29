from django.db import models


# Create your models here.

class Location(models.Model):
    zip = models.IntegerField()
    lat = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    lon = models.DecimalField(max_digits=8, decimal_places=5, null=True)
