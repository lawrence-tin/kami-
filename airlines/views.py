from rest_framework import generics, status
from rest_framework.response import Response
from .models import Airplane
from .serializers import AirplaneSerializer
import math

class AirplaneListCreateView(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def post(self, request, *args, **kwargs):
        # Extract data from the request
        data = request.data
        airplane_id = data.get('id')

        # Check if an airplane with the given ID already exists
        if Airplane.objects.filter(id=airplane_id).exists():
            return Response({"error": "Airplane with this ID already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the data using the serializer
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            # If valid, save the serializer data as a new airplane instance
            airplane = serializer.save()

            # Calculate fuel consumption and flight duration
            fuel_consumption = math.log(airplane.id) * 0.80 + 0.002 * airplane.passenger_assumptions
            flight_duration = airplane.fuel_tank_capacity() / fuel_consumption

            # Round the calculated values for response
            formatted_fuel_consumption = round(fuel_consumption, 2)
            formatted_flight_duration = round(flight_duration, 2)

            # Prepare response data
            response_data = {
                "id": airplane.id,
                "passenger_assumptions": airplane.passenger_assumptions,
                "fuel_consumption": formatted_fuel_consumption,
                "flight_duration": formatted_flight_duration
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        # If serializer is not valid, return error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AirplaneDetailView(generics.RetrieveAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def get(self, request, *args, **kwargs):
        # Get the airplane object based on the request
        airplane = self.get_object()

        # Calculate fuel consumption and flight duration
        fuel_consumption = math.log(airplane.id) * 0.80 + 0.002 * airplane.passenger_assumptions
        flight_duration = airplane.fuel_tank_capacity() / fuel_consumption

        # Round the calculated values for response
        formatted_fuel_consumption = round(fuel_consumption, 2)
        formatted_flight_duration = round(flight_duration, 2)

        # Return response data
        return Response({
            "total_fuel_consumption": formatted_fuel_consumption,  # Updated key name to match the test
            "flight_duration": formatted_flight_duration
        }, status=status.HTTP_200_OK)
