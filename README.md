# Mqtt5_BridgeServer
MQTT5 relay/bridge server 
that server external network to internat network config and act as bridge between private devices and outside device 
Home Anywhere MQTT 🛰️

Secure, lightweight home automation with MQTT on Ubuntu.
This repo shows how to deploy Eclipse Mosquitto as your broker, add auth & TLS, enable remote access (Tailscale or 8883/TLS), and wire up example publishers/subscribers.
	•	Broker: Mosquitto
	•	Remote access (choose one):
	•	A. Tailscale (recommended) – no open ports, private overlay network
	•	B. Public TLS on 8883 – for classic clients across the internet
	•	C. Cloudflare Tunnel – if you prefer tunnels over VPNs
	•	Clients: mosquitto_pub/sub, Python (paho-mqtt), Home Assistant ready

Features
	•	Pub/Sub topics with QoS 0/1/2
	•	Retained messages for last-known state
	•	Last Will to detect offline devices
	•	Auth, TLS, UFW firewall, systemd service
	•	Example topic design for rooms/devices
