from rest_framework import routers
from vehicle_services import views 
from django.urls import path,include

router = routers.DefaultRouter()


router.register(r'vehicleViewSet', views.VehicleAPIView),