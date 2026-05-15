# mqtt_client.py

# Import MQTT client library
from mqtt.simple import MQTTClient

# Import time module
import time


# Create a class to manage MQTT communication
class MQTTManager:

    # Runs when MQTTManager object is created
    def __init__(self, client_id, broker, topic):

        # Create MQTT client
        self.client = MQTTClient(client_id, broker)

        # Store topic
        self.topic = topic


    # Runs when subscribed message is received
    def callback(self, topic, msg):

        # Print received MQTT message
        print("Received:", msg)


    # Connect to MQTT broker
    def connect(self):

        # Set callback function
        self.client.set_callback(self.callback)

        # Connect to broker
        self.client.connect()

        # Subscribe to topic
        self.client.subscribe(self.topic)

        # Print successful connection message
        print("MQTT connected")


    # Publish sensor data to MQTT topic
    def publish(self, data):

        # Convert Python dictionary to string
        message = f"{data}"

        # Publish message to topic
        self.client.publish(self.topic, message)

        # Print published message
        print("Published:", message)


    # Check if new MQTT messages arrived
    def check(self):

        try:
            # Check for incoming subscribed messages
            self.client.check_msg()

        except:
            # Ignore errors for now
            pass