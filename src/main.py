#main

# Import the do_connect function from do_connect.py file
from do_connect import do_connect
# Import the secrets function from secrets.py file
from secrets import secrets
# Import the read_sensors function from sensors.py file
from sensors import read_sensors
# Im the WebServer function from web_server.py file
from web_server import WebServer

from mqtt_client import MQTTManager

#Import the time module (used for delays like sleep)
import time

# Call the do_connect function using your WiFi name and password
# secrets["ssid"] gets the WiFi name from the dictionary
# secrets["password"] gets the password from the dictionary
# The function returns the IP address (or None if failed)
ip = do_connect(secrets["ssid"], secrets["password"])

server = WebServer(ip)

mqtt = MQTTManager(
    client_id="alex_device",
    broker="test.mosquitto.org",
    topic=b"alex/smart_room"
)

mqtt.connect()

last_publish = time.ticks_ms()

# Start an infinite loop (runs forever, will be used to continuously update other readings)
while True:
    # Call read_sensors() from sensors.py to retrieve current sensor data and store it in 'data'
    data = read_sensors()
    server.check_client(data)
    mqtt.check()
    
    now = time.ticks_ms()
    
    if time.ticks_diff(now, last_publish) > 5000:
        mqtt.publish(data)
        last_publish = now
        
    print(data)
    
    time.sleep(1)
    


