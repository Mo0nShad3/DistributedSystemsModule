import paho.mqtt.client as mqtt_client # Import the repository used for MQTT. Documentation here: https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html
import json
import os
import uuid
from random import uniform, randint
import time
from datetime import datetime
import logging

# Configure the logging so that errors can be seen when deployed in the docker container
#logging.basicConfig(level=logging.INFO)

# MQTT broker configuration variables
mqtt_Broker = 'mqtt.em-solutions.co.uk' # Public IP of broker to connect.
mqtt_Port = 1885 # Non-standard port for security.
mqtt_Topic = "Clients/Client_1" # Set the topics that the server will look for
mqtt_ClientID = "SmartMeterServer100084" # Set the server ClientID
mqtt_ReturnTopic = "Clients/Client_1/Response"

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("Connected with result code {0}".format(str(rc)))
        #Print result of connection attempt
        client.subscribe(mqtt_Topic)  
        # Subscribe to the topic defined by the tag, receive any message published to it
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, message): # Callback for when a published message is recieved from a client.
    print("Message received: " + message.topic + " " + str(message.payload)) # Print the message recieved
    
    # Decode the message payload
    payload = message.payload.decode()

    # Load the decoded payload as a JSON object
    try:
        received_message = json.loads(payload)
        
        bill_Total = uniform(0,1000)

        json_Message = { # Create the JSON message
            "Client ID": f"{received_message['Client ID']}",
            "Message Topic": f"{received_message['Message Topic']}",
            "Timestamp": f"{received_message['Timestamp']}",
            "Power Consumed": f"{received_message['Power Consumed']}",
            "Publish Frequency": f"{received_message['Publish Frequency']}",
            "Bool": f"{received_message['Bool']}",
            "Bill Total": f"{bill_Total}"
        }

        print(json_Message)

        json_string = json.dumps(json_Message)

        client.publish(mqtt_ReturnTopic, json_string)
        print("Published Message")

    except json.JSONDecodeError:
        print("Error: Invalid message recieved")

def callBill(Client_ID, Topic, Timestamp, powerConsumed):
    bill_Total = (received_message['Power Consumed']*24)

def errorMessage(Client_ID, Topic, Timestamp, Error):
    errorMessage = ("Error with system")

client = mqtt_client.Client(client_id=mqtt_ClientID, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2) # Create an instance of the client with client ID "mqtt_clientID" tag
client.on_connect = on_connect # Define the callback function for sucessful connection
client.on_message = on_message # Define the callback function for reciept of a message
client.connect(mqtt_Broker, mqtt_Port, 60) # Connect to (broker, port, keepalive)
client.loop_forever() # Start a networking daemon
