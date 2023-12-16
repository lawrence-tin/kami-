====================
Usage Examples Guide
====================

This section provides usage examples for interacting with the KAMI Airlines API.

1. Inputting Airplane Data

   Use a POST request to `/api/airplanes/` with JSON data containing airplane ID and passenger assumptions to input airplane data.

   Example:

   POST /api/airplanes/
    {
    "id": 1,
    "passenger_assumptions": 100
    }


2. Retrieving Calculated Data

Use a GET request to `/api/airplanes/<id>/` to retrieve calculated fuel consumption and maximum flight duration for a specific airplane.

Example:

GET /api/airplanes/1/



