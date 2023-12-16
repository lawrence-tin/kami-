KAMI Airlines Aircraft Passenger Capacity Solution

Problem Description
KAMI Airlines is evaluating 10 different airplanes, each with varying passenger assumptions and fuel tank capacities. The objective is to create a RESTful API using Django Rest Framework that allows input for these airplanes and calculates the total airplane fuel consumption per minute along with the maximum duration each airplane can fly based on its fuel capacity and assumptions.

Requirements
- The company is assessing 10 airplanes.
- Each airplane has a fuel tank capacity of (200 liters * id of the airplane).
- Airplane fuel consumption per minute is logarithm of airplane id multiplied by 0.80 liters.
- Each passenger increases fuel consumption by an additional 0.002 liters per minute.

Features
The solution includes the following functionalities:

Endpoints
1. Input of Airplanes
   - Route: `/api/airplanes/`
   - Method: POST
   - Accepts input for 10 airplanes with user-defined ID and passenger assumptions.

2. Calculations
   - Route: `/api/airplanes/<id>/`
   - Method: GET
   - Provides total airplane fuel consumption per minute and the maximum minutes each airplane is able to fly based on its fuel capacity and assumptions.

Setup Instructions
Follow these steps to run the code:

Prerequisites
- Python 3.x
- Django
- Django Rest Framework

Installation
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.

Run the Server
1. Navigate to the project directory.
2. Run the Django development server using `python manage.py runserver`.

Usage
- Access the API endpoints using a tool like cURL, Postman, or any REST client.
- Use POST request to `/api/airplanes/` to input airplane data.
- Use GET request to `/api/airplanes/<id>/` to calculate fuel consumption and maximum flight duration for a specific airplane.

Notes
- Ensure all necessary data for the airplanes (ID, passenger assumptions) are provided during input.
- Responses from the API will include calculated fuel consumption per minute and maximum flight duration.
