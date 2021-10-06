from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','make','model','year','user_id', 
            'color', 'mileage','license_plate','VIN','maintenance_cost']