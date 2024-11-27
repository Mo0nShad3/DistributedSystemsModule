import unittest
import paho.mqtt.client as mqtt_client
import json
import logging

# MQTT broker configuration variables
mqtt_Broker = 'mqtt.em-solutions.co.uk'  # Public IP of broker to connect.
mqtt_Port = 1885  # Non-standard port for security.
mqtt_Topic = "Clients/Client_1"  # Set the topics that the server will look for
mqtt_ClientID = "SmartMeterServer100084"  # Set the server ClientID
mqtt_ReturnTopic = "Clients/Client_1/Response"

#Establish logging
logging.basicConfig(level=logging.INFO)

def callBill(powerConsumed):
    bill_Total = powerConsumed * (24 * 60 * 60 / 45) #45sec intervals 24hrs
    return bill_Total

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        logging.info(f"Connected with result code {rc}")
        #Print result of connection attempt
        client.subscribe(mqtt_Topic)  
        # Subscribe to the topic defined by the tag, receive any message published to it
    else:
        logging.error(f"Failed to connect, return code {rc}")

def on_message(client, userdata, message):  # Callback for when a published message is received from a client.
    logging.info(f"Message received: {message.topic} {str(message.payload)}")

    # Decode the message payload
    try:
        payload = json.loads(message.payload.decode())

        # Simulate `callBill` function
        powerConsumed = float(payload["Power Consumed"])
        bill_Total = callBill(powerConsumed)

        response_message = {
            "Client ID": payload["Client ID"],
            "Message Topic": payload["Message Topic"],
            "Timestamp": payload["Timestamp"],
            "Power Consumed": powerConsumed,
            "Publish Frequency": payload["Publish Frequency"],
            "Bool": payload["Bool"],
            "Bill Total": bill_Total
        }

        # Publish the response message to the return topic
        client.publish(mqtt_ReturnTopic, json.dumps(response_message))

    except json.JSONDecodeError:
        logging.error("Error: Invalid message received")
    except KeyError as e:
        logging.error(f"Missing key in message payload: {e}")


def create_mqtt_client():
    client = mqtt_client.Client(mqtt_ClientID)
    client.on_connect = on_connect  # Define the callback function for successful connection
    client.on_message = on_message  # Define the callback function for receipt of a message
    return client

class TestCallBill(unittest.TestCase):
    def test_call_bill(self):
        powerConsumed = 5.0
        expected_bill_total = 5.0 * (24 * 60 * 60 / 45)  #45 sec intervals, 24 hours
        result = callBill(powerConsumed)
        self.assertAlmostEqual(result, expected_bill_total)

    def test_call_bill_zero(self):
        #zero bill
        powerConsumed = 0.0
        expected_bill_total = 0.0
        result = callBill(powerConsumed)
        self.assertEqual(result, expected_bill_total)

    def test_call_bill_large(self):
        #Large bill
        powerConsumed = 100.0
        expected_bill_total = 100.0 * (24 * 60 * 60 / 45)
        result = callBill(powerConsumed)
        self.assertAlmostEqual(result, expected_bill_total)

if __name__ == '__main__':
    client = create_mqtt_client()
    client.connect(mqtt_Broker, mqtt_Port, 60)
    client.loop_start()  #non-blocking

    unittest.main()
