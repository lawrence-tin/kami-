from django.db import models
import math

class Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    passenger_assumptions = models.IntegerField()

    def fuel_tank_capacity(self):
        """
        Calculates the fuel tank capacity based on the airplane's ID.
        Formula: 200 * ID
        """
        return 200 * self.id

    def fuel_consumption_per_minute(self):
        """
        Calculates the fuel consumption per minute based on the airplane's ID and passenger assumptions.
        Formula: log(ID) * 0.80 + 0.002 * passenger_assumptions
        """
        return math.log(self.id) * 0.80 + 0.002 * self.passenger_assumptions
