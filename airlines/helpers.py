import math
from .models import Airplane

def calculate_expected_fuel_consumption() -> float:
    """
    Calculate the expected total fuel consumption based on sample data.
    
    Returns:
    float: Expected total fuel consumption.
    """
    return 0.80 * math.log(1) + 0.002 * 100 + 0.80 * math.log(2) + 0.002 * 150

# Optional docstring based on your implementation needs
def calculate_flight_data(airplane: Airplane) -> dict:
    """
    Calculate flight data based on an airplane instance.
    
    Args:
    airplane (Airplane): An instance of Airplane model.
    
    Returns:
    dict: Flight data including fuel consumption and duration.
    """
    fuel_consumption = airplane.fuel_consumption_per_minute()
    flight_duration = airplane.fuel_tank_capacity() / fuel_consumption

    formatted_fuel_consumption = round(fuel_consumption, 2)
    formatted_flight_duration = round(flight_duration, 2)

    return {
        "id": airplane.id,
        "passenger_assumptions": airplane.passenger_assumptions,
        "fuel_consumption": formatted_fuel_consumption,
        "flight_duration": formatted_flight_duration
    }
