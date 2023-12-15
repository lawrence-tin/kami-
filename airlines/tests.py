from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Airplane
import math

class AirplaneAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Creating sample airplanes for testing
        Airplane.objects.create(id=1, passenger_assumptions=100)
        Airplane.objects.create(id=2, passenger_assumptions=150)
        
    def test_invalid_airplane_data(self):
        # Test creating an airplane with invalid data
        data = {'id': 4}  # Missing 'passenger_assumptions'
        response = self.client.post('/api/airplanes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Add assertions to validate the error response if needed

    def test_create_airplane(self):
        # Test creating a new airplane
        data = {'id': 3, 'passenger_assumptions': 120}
        response = self.client.post('/api/airplanes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_existing_airplane(self):
        # Test creating an airplane with an existing ID
        data = {'id': 1, 'passenger_assumptions': 100}
        response = self.client.post('/api/airplanes/', data, format='json')

        # Ensure the response status code is as expected (HTTP 400 Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check the response content or specific error message
        expected_response_data = {"error": "Airplane with this ID already exists"}
        self.assertEqual(response.data, expected_response_data)


    def test_get_airplane_details(self):
        # Test retrieving airplane details
        response = self.client.get('/api/airplanes/1/')
        
        # Check if the request was successful (HTTP 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add assertions to validate response data as needed
        # For instance, if you expect certain keys or values in the response data:
        expected_data = {
            "id": 1,
            "passenger_assumptions": 100,  # Update with your expected values
            # Add more expected keys and values as needed
        }
        self.assertEqual(response.data, expected_data)


    
