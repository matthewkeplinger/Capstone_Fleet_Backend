from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import VehicleService
from .serializers import VehicleServiceSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_service_records(request):
    vehicle_services = VehicleService.objects.all()
    serializer = VehicleServiceSerializer(vehicle_services, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def vehicle_service_records(request):
    if request.method == 'POST':
        serializer = VehicleServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        vehicles = VehicleService.objects.filter(vehicle_id=request.vehicle.id)
        serializer = VehicleServiceSerializer(vehicles, many = True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_vehicle_history(request, vehicle_id):
    vehicle_services = VehicleService.objects.filter(vehicle_id=vehicle_id)
    serializer = VehicleServiceSerializer(vehicle_services, many=True)
    return Response(serializer.data)