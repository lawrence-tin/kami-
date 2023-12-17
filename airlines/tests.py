from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Airplane
import math

class AirplaneAPITests(TestCase):
    """
    Test cases for the Airplane API functionality.
    """
    def setUp(self):
        """
        Set up sample airplanes for testing.
        """
        self.client = APIClient()
        Airplane.objects.create(id=1, passenger_assumptions=100)
        Airplane.objects.create(id=2, passenger_assumptions=150)
        
    def test_invalid_airplane_data(self):
        """
        Test creating an airplane with invalid data.
        """
        data = {'id': 4}  # Missing 'passenger_assumptions'
        response = self.client.post('/api/airplanes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_airplane(self):
        """
        Test creating a new airplane.
        """
        data = {'id': 3, 'passenger_assumptions': 120}
        response = self.client.post('/api/airplanes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_existing_airplane(self):
        """
        Test creating an airplane with an existing ID.
        """
        data = {'id': 1, 'passenger_assumptions': 100}
        response = self.client.post('/api/airplanes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_response_data = {"error": "Airplane with this ID already exists"}
        self.assertEqual(response.data, expected_response_data)

    def test_get_airplane_details(self):
        """
        Test retrieving airplane details.
        """
        response = self.client.get('/api/airplanes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_airplane(self):
        """
        Test deleting an airplane by ID.
        """
        response = self.client.delete('/api/airplanes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
