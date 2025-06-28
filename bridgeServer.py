from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

INTERNAL_SERVER_URL = "https://serverIP:8443/mqtt/publish"
# Use internal IP or DNS

@app.route('/bridge/publish', methods=['POST'])
def bridge_publish():
    data = request.json
    try:
        resp = requests.post(
            INTERNAL_SERVER_URL,
            json=data,
            verify=False  # For self-signed certs; set to True with valid certs
        )
        return (resp.text, resp.status_code, resp.headers.items())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Expose this server to the internet (use HTTPS in production)
    app.run(host='0.0.0.0', port=5000)
