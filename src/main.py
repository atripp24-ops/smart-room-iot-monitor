# main.py

from do_connect import do_connect
from secrets import secrets
from sensors import read_sensors
from web_server import WebServer
from mqtt_client import MQTTManager
import time

# Connect to WiFi and store the Pico W IP address
ip = do_connect(secrets["ssid"], secrets["password"])

# Stop program if WiFi connection failed
if ip is None:
    print("WiFi failed. Cannot start web server or MQTT.")
    raise SystemExit

# Start local web server using Pico W IP address
server = WebServer(ip)

# Set up MQTT connection
mqtt = MQTTManager(
    client_id="alex_device",
    broker="test.mosquitto.org",
    topic=secrets["mqtt_topic"]
)

mqtt.connect()

# Track last MQTT publish time
last_publish = time.ticks_ms()

# Main system loop
while True:
    # Read latest sensor values
    data = read_sensors()

    # Check if a browser requested the webpage
    server.check_client(data)

    # Check for incoming MQTT messages
    mqtt.check()

    # Publish data every 5 seconds
    now = time.ticks_ms()

    if time.ticks_diff(now, last_publish) > 5000:
        mqtt.publish(data)
        last_publish = now

    # Print values in Thonny Shell for debugging
    print(data)

    time.sleep(1)