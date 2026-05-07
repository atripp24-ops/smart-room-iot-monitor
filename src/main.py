#main

# Import the do_connect function from do_connect.py file
from do_connect import do_connect
# Import the secrets function from secrets.py file
from secrets import secrets
#Import the time module (used for delays like sleep)
import time

# Call the do_connect function using your WiFi name and password
# secrets["ssid"] gets the WiFi name from the dictionary
# secrets["password"] gets the password from the dictionary
# The function returns the IP address (or None if failed)
ip = do_connect(secrets["ssid"], secrets["password"])

# Start an infinite loop (runs forever, will be used to continuously update other readings)
while True:
    # Call read_sensors() from sensors.py to retrieve current sensor data and store it in 'data'
    data = read_sensors()
    print(data)
    time.sleep(3)
    
