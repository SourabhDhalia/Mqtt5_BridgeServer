// // Simple MQTT bridge/gateway
// const mqtt = require('mqtt');

// // External-facing MQTT server (simulated "outside")
// // Replace '0.0.0.0' with your Mac/PC's local IP if you want to allow other devices
// const aedes = require('aedes')();
// const net = require('net');
// net.createServer(aedes.handle).listen(1884, () => {
//   console.log('Gateway listening on port 1884 (external)');
// });

// // Internal broker connection (simulated company LAN)
// const internalClient = mqtt.connect('mqtt://localhost:1883'); // Mosquitto default port

// aedes.on('publish', (packet, client) => {
//   if (client) {
//     // Forward any message published by external client to internal broker
//     internalClient.publish(packet.topic, packet.payload);
//   }
// });

// mqtt_gateway.js
const mqtt = require('mqtt');
const aedes = require('aedes')();
const net = require('net');

// Start gateway broker (external port 1884)
net.createServer(aedes.handle).listen(1885, () => {
  console.log('Gateway listening on port 1885');
});

// Connect to internal broker (Windows Laptop IP, port 1883)
const INTERNAL_BROKER_IP = '172.16.2.43'; // Replace with your Windows laptop’s IP
const internalClient = mqtt.connect(`mqtt://${INTERNAL_BROKER_IP}:1883`);

// Forward external publishes to internal broker
aedes.on('publish', (packet, client) => {
  if (client) {
    internalClient.publish(packet.topic, packet.payload);
  }
});