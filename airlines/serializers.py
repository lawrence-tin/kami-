from rest_framework import serializers
from .models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane  # Specifies the model associated with the serializer
        fields = ['id', 'passenger_assumptions']  # Defines the fields to be serialized/deserialized
