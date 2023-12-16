from django.db import models
import math

class Airplane(models.Model):
    """
    Model representing an airplane.
    """
    id = models.IntegerField(primary_key=True)
    passenger_assumptions = models.IntegerField()

    def fuel_tank_capacity(self) -> int:
        """
        Calculate the fuel tank capacity based on the airplane's ID.
        
        Returns:
        int: Fuel tank capacity.
        
        """
        return 200 * self.id

    def fuel_consumption_per_minute(self) -> float:
        """
        Calculate the fuel consumption per minute.
        
        Returns:
        float: Fuel consumption per minute.
        """
        return math.log(self.id) * 0.80 + 0.002 * self.passenger_assumptions
