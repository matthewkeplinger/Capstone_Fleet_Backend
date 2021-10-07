from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    make = models.CharField(max_length =30)
    model = models.CharField(max_length =100)
    year = models.IntegerField()
    color = models.CharField(max_length = 50)
    mileage = models.IntegerField()
    license_plate = models.CharField(max_length = 30)
    VIN = models.CharField(max_length = 17)
    maintenance_cost = models.IntegerField()

    def __str__(self):
        return self.body