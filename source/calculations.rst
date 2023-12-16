The KAMI Airlines solution calculates fuel consumption per minute and maximum flight duration for each airplane based on the following specifications:

- Each airplane's fuel tank capacity is determined by the formula: `200 liters * airplane_id`.
- Fuel consumption per minute is calculated as the logarithm of the airplane ID multiplied by 0.80 liters.
- Additional passengers increase fuel consumption by an extra 0.002 liters per minute.
