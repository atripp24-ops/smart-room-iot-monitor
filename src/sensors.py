# sensors.py

import random

def read_sensors():

    # Fake temperature between 68F and 80F
    temp = random.randint(68, 80)

    # Fake humidity between 40% and 70%
    humidity = random.randint(40, 70)

    # Randomly choose occupied or empty
    motion = random.choice([True, False])

    return {
        "temp": temp,
        "humidity": humidity,
        "motion": motion
    }