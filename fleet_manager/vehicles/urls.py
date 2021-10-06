from django.conf.urls import url
from django.urls import path
from vehicles import views

urlpatterns = [
    path('all/', views.get_all_vehicles),
    path('my-garage/', views.user_vehicles),
]