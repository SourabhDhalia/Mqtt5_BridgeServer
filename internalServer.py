from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

MQTT_BROKER = "BridgeServerIP"
MQTT_PORT = 1883

mqtt_client = mqtt.Client(protocol=mqtt.MQTTv5)
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
mqtt_client.loop_start()

@app.route('/mqtt/publish', methods=['POST'])
def mqtt_publish():
    data = request.json
    topic = data.get('topic')
    message = data.get('message')
    if not topic or not message:
        return jsonify({'error': 'Missing topic or message'}), 400
    result = mqtt_client.publish(topic, str(message), qos=1)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        return jsonify({'status': 'Published'}), 200
    return jsonify({'error': 'MQTT publish failed'}), 500

if __name__ == '__main__':
    # Use SSL context for HTTPS (provide your cert and key)
    app.run(host='0.0.0.0', port=8443, ssl_context=('cert.pem', 'key.pem'))
