from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Vehicle
from .serializers import VehicleSerializer
from django.contrib.auth.models import User
from vehicle_services.serializers import VehicleServiceSerializer
from vehicle_services.models import VehicleService


# from rest_framework import viewsets
# from rest_framework import generics
# from rest_framework import filters



@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_vehicles(request):
    print('get_all_vehicles METHOD HIT')
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_object(self,pk):
    print('get_object METHOD HIT')
    try:
        return Vehicle.objects.filter(pk=pk)
    except Vehicle.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def get(request, pk):
    print('get METHOD HIT')
    vehicle = Vehicle.objects.filter(pk=pk)
    serializer = VehicleSerializer(vehicle, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_vehicles(request):
    print('User', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        vehicles = Vehicle.objects.filter(user_id=request.user.id)
        serializer = VehicleSerializer(vehicles, many = True)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_vehicle(request):
    if request.method == 'PUT':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    



