from rest_framework import serializers
from .models import VehicleService
from services.serializers import ServiceSerializer

class VehicleServiceSerializer(serializers.ModelSerializer):

    service_type = serializers.ReadOnlyField(source='service_id.service_type')
    mileage_interval = serializers.ReadOnlyField(source='service_id.mileage_interval')
    service_cost = serializers.ReadOnlyField(source='service_id.service_cost')
    part_used = serializers.ReadOnlyField(source='service_id.part_used')
    class Meta:
        model = VehicleService
        #3fields = "__all__"
        fields = ["url",'id','vehicle_id','service_id','mileage_performed','date_performed','service_type', 'mileage_interval', 'service_cost', 'part_used']