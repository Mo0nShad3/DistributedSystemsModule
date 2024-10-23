import paho.mqtt.client as mqtt_client
import json
import os
import uuid 
from random import uniform, randint
import time
from datetime import datetime
import logging

# Configure logging so that errors can be seen in the docker log.
logging.basicConfig(level=logging.INFO)

# MQTT broker configuration 
mqtt_Broker = 'mqtt.em-solutions.co.uk' # Public IP of broker to connect to.
mqtt_Port = 1885 # Non-standard port for security.
client_ID = "Client_" + "1"  #str(uuid.uuid4()) # Set a unique client ID ~ 

mqtt_Topic = f'Clients/{client_ID}' # Set the mqtt topic to send its' data to 
mqtt_ReturnTopic = f'Clients/{client_ID}/Response' # Set the topic that messages are recieved on
mqtt_ErrorTopic = f'Clients/{client_ID}/Error' # Set the topic where error messages are sent to

# Output the client id to the log
logging.info(f"Client ID: {client_ID}")

# Tag to store the publish count
publish_Count = int(0)

# Function to handle received messages
def on_message(client, userdata, message):
    received_message = json.loads(message.payload.decode()) # Decode any message received

    if (message.topic == mqtt_ReturnTopic): # Check if the message has been recieved from the same clients ID
        bill_Total = received_message['Bill Total']
        if bill_Total: # Check if Bill Total exists in the message
            logging.info(f'Recieved message:  {bill_Total}') # Act on the received message
        else:
            logging.info(f'Recieved message without the bill total, {recieved_message}')
    elif (message.topic == mqtt_ErrorTopic):
        error_Message = received_message['Error Message']
        if error_Message: # Check if there is an error message
            logging.info(f'Error: {error_Message}') # Output the error message if one is found
        else:
            logging.info(f'Invalid message format')
    else:
        logging.info(f'Invalid Message: Not from client')
        # If the message is not from either topic do nothing

# Set the on_message callback
client = mqtt_client.Client()
client.on_message = on_message

# Connect to the broker
client.connect(mqtt_Broker, mqtt_Port)

# Subscribe to the topic to receive messages
client.subscribe(mqtt_ReturnTopic)
client.subscribe(mqtt_ErrorTopic)

# Start the network loop to enable message reception
client.loop_start()

while True: # Main loop
    power_Consumed = uniform(2,7) # Power consumed per 45s in w/h
    publish_Time = randint(15,45) # Publish time randomly generated between 15 and 45 seconds
    timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    json_Message = { # Create the JSON message
        "Client ID": f"{client_ID}",
        "Message Topic": f"{mqtt_Topic}",
        "Timestamp": f"{timeStamp}",
        "Power Consumed": f"{power_Consumed}",
        "Publish Frequency": f"{publish_Time}",
        "Bool": True
    }

    json_string = json.dumps(json_Message)

    client.publish(mqtt_Topic, json_string)
    publish_Count = publish_Count + 1
    logging.info(client_ID)

    logging.info(f"Published message: {publish_Count}, {timeStamp}, Next message will be sent in {publish_Time} seconds.")

    time.sleep(publish_Time)


# Stop the network loop when exiting the application
client.loop.stop()
