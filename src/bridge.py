from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import json
import config

app = Flask(__name__)

# MQTT v5 client setup
def on_connect(client, userdata, flags, reasonCode, properties):
    print(f"Connected to MQTT broker (MQTT v5) with reason code: {reasonCode}")

mqtt_client = mqtt.Client(protocol=mqtt.MQTTv5)
mqtt_client.on_connect = on_connect

if getattr(config, "MQTT_USERNAME", None) and getattr(config, "MQTT_PASSWORD", None):
    mqtt_client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)

mqtt_client.loop_start()
mqtt_client.connect(config.MQTT_BROKER, config.MQTT_PORT, 60)

@app.route('/publish', methods=['POST'])
def publish():
    data = request.json
    topic = data.get('topic')
    message = data.get('message')

    if not topic or not message:
        return jsonify({'error': 'Topic and message are required'}), 400

    # Publish as string (no double JSON encoding)
    result = mqtt_client.publish(topic, str(message), qos=1, properties=None)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        return jsonify({'status': 'Message published successfully'}), 200
    else:
        return jsonify({'error': 'Failed to publish message'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=getattr(config, "HTTP_PORT", 5000))