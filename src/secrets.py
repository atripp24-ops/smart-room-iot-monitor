#secrets

# Create a dictionary called "secrets" to store important configuration values
secrets = {
    # "ssid" is the name of your WiFi network (what you see when connecting on your phone)
    "ssid" : "YOUR_WIFI_NAME"
    # "password" is the password for your WiFi network
    "password" : "YOUR_WIFI_PASSWORD"
    # "mqtt_topic" is the channel/topic your device will use to send and receive data
    # The b"" means this is a byte string (required by MQTT in MicroPython)
    "mqtt_topic" : b"alex/smart_room"
    }