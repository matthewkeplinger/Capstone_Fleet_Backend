from django.conf.urls import url
from django.urls import path
from services import views

urlpatterns = [
    path('all/', views.get_all_services),
    path('', views.vehicle_services),
]