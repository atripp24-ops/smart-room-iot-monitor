#mqtt_client

# Import the MQTTClient class from the MicroPython MQTT library.
# This lets the Pico W connect to an MQTT broker, publish messages, and subscribe to topics.
from umqtt.simple import MQTTClient

# Import time module.
# Not currently used in this file, so you can remove it unless you use it later.
import time


# Create a class to manage MQTT communication.
class MQTTManager:

    # __init__ runs when you create an MQTTManager object.
    # client_id = unique name for your Pico device
    # broker = MQTT server address, example: "test.mosquitto.org"
    # topic = MQTT topic/channel where messages are sent and received
    def __init__(self, client_id, broker, topic):

        # Create an MQTT client object using the device name and broker address.
        self.client = MQTTClient(client_id, broker)

        # Store the topic so other methods can use it later.
        self.topic = topic


    # This function runs automatically when a subscribed MQTT message is received.
    # topic = the topic/channel where the message came from
    # msg = the actual message received
    def callback(self, topic, msg):

        # Print the message received from MQTT.
        print("Received:", msg)


    # Connect to the MQTT broker and subscribe to the topic.
    def connect(self):

        # Tell the MQTT client what function to call when a message arrives.
        self.client.set_callback(self.callback)

        # Connect to the MQTT broker.
        self.client.connect()

        # Subscribe to the topic so this Pico can receive messages from it.
        self.client.subscribe(self.topic)

        # Print