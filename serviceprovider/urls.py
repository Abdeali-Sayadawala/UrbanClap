from django.urls import path, include
from .views import spregister

urlpatterns = [
    path('spregister/', spregister)
]