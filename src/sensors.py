# sensors.py

# Import Pin class for GPIO communication
from machine import Pin

# Import DHT sensor library
import dht


# Create DHT11 sensor object connected to GPIO 15
dht_sensor = dht.DHT11(Pin(15))

# Create PIR motion sensor object connected to GPIO 14
pir = Pin(14, Pin.IN)


# Function that reads all sensor data
def read_sensors():

    # Tell the DHT11 to take a new measurement
    dht_sensor.measure()

    # Read temperature in Celsius
    temp_c = dht_sensor.temperature()

    # Read humidity percentage
    humidity = dht_sensor.humidity()

    # Convert Celsius to Fahrenheit
    temp_f = (temp_c * 9 / 5) + 32

    # Read PIR motion sensor value
    # 1 = motion detected
    # 0 = no motion detected
    motion = pir.value()

    # Return all sensor values as a dictionary
    return {
        "temp": round(temp_f, 1),
        "humidity": humidity,
        "motion": bool(motion)
    }