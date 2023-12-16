The KAMI Airlines RESTful API offers the following endpoints:

1. Input of Airplanes

   - Route: `/api/airplanes/`
   - Method: POST
   - Description: Allows input for 10 airplanes with user-defined ID and passenger assumptions.

2. Calculations

   - Route: `/api/airplanes/<id>/`
   - Method: GET
   - Description: Provides total airplane fuel consumption per minute and maximum flight duration for a specific airplane based on its fuel capacity and assumptions.
