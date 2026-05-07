#sensors

import random

def read_sensors():
    return{
        "temp": random.randint(70,85),
        "humidity": random.randint(40,70),
        "motion": random.randint([True,False])
        }