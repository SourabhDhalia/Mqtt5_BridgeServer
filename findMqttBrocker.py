from zeroconf import ServiceBrowser, Zeroconf

class MQTTListener:
    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            print(f"Discovered MQTT broker: {info.server} at {socket.inet_ntoa(info.addresses[0])}:{info.port}")

zeroconf = Zeroconf()
listener = MQTTListener()
browser = ServiceBrowser(zeroconf, "_mqtt._tcp.local.", listener)
input("Press enter to exit...\n")
zeroconf.close()