from rest_framework import serializers
from .models import VehicleService

class VehicleServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleService
        fields = ['vehicle_id','service_id','mileage_performed','date_performed']