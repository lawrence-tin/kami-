from rest_framework import generics, status
from rest_framework.response import Response
from .models import Airplane
from .serializers import AirplaneSerializer
import math

class AirplaneListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating airplanes.
    """
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def post(self, request, *args, **kwargs):
        """
        Create a new airplane.
        """
        data = request.data
        airplane_id = data.get('id')

        if Airplane.objects.filter(id=airplane_id).exists():
            return Response({"error": "Airplane with this ID already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            airplane = serializer.save()

            # Calculate flight-related data
            fuel_consumption = math.log(airplane.id) * 0.80 + 0.002 * airplane.passenger_assumptions
            flight_duration = airplane.fuel_tank_capacity() / fuel_consumption

            formatted_fuel_consumption = round(fuel_consumption, 2)
            formatted_flight_duration = round(flight_duration, 2)

            response_data = {
                "id": airplane.id,
                "passenger_assumptions": airplane.passenger_assumptions,
                "fuel_consumption": formatted_fuel_consumption,
                "flight_duration": formatted_flight_duration
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AirplaneDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting airplane details.
    """
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def get(self, request, *args, **kwargs):
        """
        Retrieve details of a specific airplane.
        """
        airplane = self.get_object()

        # Calculate flight-related data
        fuel_consumption = math.log(airplane.id) * 0.80 + 0.002 * airplane.passenger_assumptions
        flight_duration = airplane.fuel_tank_capacity() / fuel_consumption

        formatted_fuel_consumption = round(fuel_consumption, 2)
        formatted_flight_duration = round(flight_duration, 2)

        return Response({
            "total_fuel_consumption": formatted_fuel_consumption,
            "flight_duration": formatted_flight_duration
        }, status=status.HTTP_200_OK)
