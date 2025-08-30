"""
Configuration settings for the HTTP to MQTT bridge.

These names align with the README and the bridge implementation.
Update values as needed for your environment.
"""

# MQTT broker connection
MQTT_BROKER = "localhost"
MQTT_PORT = 1883

# Optional authentication
# MQTT_USERNAME = "your_username"
# MQTT_PASSWORD = "your_password"

# Optional HTTP server port (defaults to 5000 if unset)
# HTTP_PORT = 5000

# Default topic for examples/tests (not required by the app)
MQTT_TOPIC = "test/topic"
