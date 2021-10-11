from django.conf.urls import url
from django.urls import path
from vehicle_services import views

urlpatterns = [
    path('all/', views.get_all_service_records),
    path('', views.vehicle_service_records),
    path('<int:vehicle_id>/', views.get_vehicle_history),
]