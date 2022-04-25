from django.db import models
from django.contrib.gis.db import models


class Clinic(models.Model):

    name = models.CharField(max_length=255)
    street =models.CharField(max_length=255)
    no_adres = models.CharField(max_length=50)
    city = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name



