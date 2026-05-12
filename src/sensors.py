#sensors

from machine import pin
import dht

# DHT11 connected to GP15
dht_sensor = dht.DHT11(Pin(15))

# PIR sensor connected to GP14
pir = Pin(14, Pin.IN)

def read_sensors():
    
    # Read DHT11 values
    dht_sensor.measure()
    
    temp_c = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    
    # Convert celcius to Fahrenheit
    temp_f = (temp_c * 9/5) + 32
    
    # Read motion sensor
    motion = pir.value()
    
    return{
        "temp" : round(temp_f, 1) ,
        "humidity" : humidity,
        "motion" : bool(motion)
        }