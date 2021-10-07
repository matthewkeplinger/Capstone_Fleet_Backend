from django.db import models

# Create your models here.
class Service(models.Model):
    service_type = models.CharField(max_length =200)
    mileage_interval = models.IntegerField()
    service_cost = models.IntegerField()
    part_used = models.CharField(max_length = 100)

    def __str__(self):
        return self.body