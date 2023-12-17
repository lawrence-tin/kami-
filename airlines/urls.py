from django.urls import path
from .views import AirplaneListCreateView, AirplaneDetailView

urlpatterns = [
    # Endpoint for listing and creating airplanes
    path('airplanes/', AirplaneListCreateView.as_view(), name='airplane-list-create'),
    
    # Endpoint for retrieving details of a specific airplane
    path('airplanes/<int:pk>/', AirplaneDetailView.as_view(), name='airplane-detail'),
    
]
