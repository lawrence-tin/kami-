from rest_framework import serializers
from .models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    """
    Serializer for the Airplane model.
    """
    class Meta:
        model = Airplane
        fields = ['id', 'passenger_assumptions']
