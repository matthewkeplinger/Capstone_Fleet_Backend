from django.db import models


# Create your models here.
class VehicleService(models.Model):
    vehicle_id = models.ForeignKey('vehicles.Vehicle', on_delete = models.CASCADE, null= True)
    service_id = models.ForeignKey('services.Service', on_delete = models.CASCADE, null = True)
    mileage_performed = models.IntegerField()
    date_performed = models.DateField()

    # def __str__(self):
    #     return self.body