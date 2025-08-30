# HTTP to MQTT Bridge

This project implements an HTTP to MQTT bridge that allows you to send data from HTTP requests to an MQTT broker. It sets up a simple HTTP server that listens for incoming requests and publishes the received data to the specified MQTT topic.

## Project Structure

```
http-mqtt-bridge
├── src
│   ├── bridge.py        # Main logic for the HTTP to MQTT bridge
│   └── config.py        # Configuration settings for the bridge
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Requirements

To run this project, you need to install the following dependencies:

- Flask: A lightweight WSGI web application framework.
- paho-mqtt: A client library for MQTT.

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/http-mqtt-bridge.git
   cd http-mqtt-bridge
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Configure the MQTT settings in `src/config.py`:

   - Set the `MQTT_BROKER` variable to your MQTT broker address.
   - Set the `MQTT_PORT` variable to the port your MQTT broker is listening on.
   - If authentication is required, set the `MQTT_USERNAME` and `MQTT_PASSWORD`.

## Running the Bridge

To start the HTTP to MQTT bridge, run the following command:

```
python src/bridge.py
```

The server will start listening for incoming HTTP requests. You can send data to the bridge using a tool like `curl` or Postman.

## Usage Example

To send a message to the MQTT broker, you can use the following `curl` command:

```
curl -X POST http://localhost:5000/publish -H "Content-Type: application/json" -d '{"topic": "test/topic", "message": "Hello, MQTT!"}'
```

This will publish the message "Hello, MQTT!" to the topic "test/topic" on your MQTT broker.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.