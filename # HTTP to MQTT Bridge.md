# HTTP to MQTT Bridge

A simple, production-ready HTTP-to-MQTT bridge built with Python, Flask, and paho-mqtt.  
This project lets you send HTTP POST requests and have them published as MQTT messages to any MQTT v5 broker.

---

## Features

- **MQTT v5 support** (using paho-mqtt)
- **RESTful HTTP API** for publishing messages
- **Configurable broker address, port, and credentials**
- **Easy to run locally or in the cloud**
- **ngrok integration** for secure public testing
- **Service discovery example** (mDNS/Bonjour)
- **Security best practices** (see below)

---

## Project Structure

```
http-mqtt-bridge/
├── src/
│   ├── bridge.py        # Main HTTP-to-MQTT bridge logic
│   └── config.py        # Configuration settings
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Quick Start

### 1. **Clone the Repository**

```sh
git clone https://github.com/yourusername/http-mqtt-bridge.git
cd http-mqtt-bridge
```

### 2. **Install Dependencies**

```sh
pip install -r requirements.txt
```

### 3. **Configure the Bridge**

Edit `src/config.py`:

```python
MQTT_BROKER_ADDRESS = "localhost"  # or your broker's IP
MQTT_BROKER_PORT = 1883
# MQTT_USERNAME = "your_username"
# MQTT_PASSWORD = "your_password"
MQTT_TOPIC = "test/topic"
```

### 4. **Run the Bridge**

```sh
python src/bridge.py
```

The server will listen on `http://localhost:5000/publish` by default.

---

## Usage Example

Send a message to your MQTT broker:

```sh
curl -X POST http://localhost:5000/publish \
  -H "Content-Type: application/json" \
  -d '{"topic": "test/topic", "message": "Hello, MQTT!"}'
```

---

## Exposing the Bridge with ngrok (for Testing)

1. [Download ngrok](https://ngrok.com/download) and install it.
2. Start ngrok to tunnel HTTP traffic to your bridge:

   ```sh
   ngrok http 5000
   ```

3. Use the public URL provided by ngrok (e.g., `https://abcd1234.ngrok.io/publish`) to send requests from anywhere.

---

## Service Discovery Example

If your MQTT brokers advertise themselves via mDNS/Bonjour, you can use the included `findMqttBrocker.py` to discover them on your LAN.

```sh
python findMqttBrocker.py
```

---

## Security Best Practices

- **Never commit sensitive files** (cert.pem, key.pem, .env, passwords) to GitHub.
- **Use HTTPS** in production and valid SSL certificates.
- **Add authentication** (API keys, JWT, etc.) to your HTTP endpoints.
- **Restrict access** to your bridge server using firewalls or security groups.
- **Monitor logs** for suspicious activity.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License.

---

## Learning Resources

- [MQTT v5 Specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [paho-mqtt Documentation](https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)
- [ngrok Documentation](https://ngrok.com/docs)
- [zeroconf Python Library](https://pypi.org/project/zeroconf/)

---

## Authors

- [Sourabh Dhalia](https://github.com/SourabhDhalia)