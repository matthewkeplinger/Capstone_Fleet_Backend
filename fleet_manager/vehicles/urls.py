from django.conf.urls import url
from django.urls import path
from vehicles import views
from . import views

urlpatterns = [
    path('all/', views.get_all_vehicles),
    path('get/<int:pk>', views.get),
    path('my-garage/', views.user_vehicles),
    path('update/<int:pk>', views.update_vehicle),
]