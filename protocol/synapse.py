# synapse.py: Custom synapse for forecast queries/responses
from bittensor import Synapse

class ForecastSynapse(Synapse):
    query: dict  # e.g., {"location": "Port Harcourt", "type": "flood_risk"}
    prediction: dict  # e.g., {"prob": 0.75}