<<<<<<< HEAD
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
    bill_Total = received_message['Power Consumed']*(60*60/45)*24 #Power consumed in 24 hours in W/h
                                                    #45sec intervals

def errorMessage(Client_ID, Topic, Timestamp, Error):
    errorMessage = ("Error with system")

client = mqtt_client.Client(client_id=mqtt_ClientID, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2) # Create an instance of the client with client ID "mqtt_clientID" tag
client.on_connect = on_connect # Define the callback function for sucessful connection
client.on_message = on_message # Define the callback function for reciept of a message
client.connect(mqtt_Broker, mqtt_Port, 60) # Connect to (broker, port, keepalive)
client.loop_forever() # Start a networking daemon
=======
import paho.mqtt.client as mqtt_client
import json
import os
import uuid 
from random import uniform, randint
import time
from datetime import datetime, timedelta
import logging
import customtkinter
import threading

user = "Admin"
client_ID = ""

# This is set based on messages received from the  client
status = True

# Configure logging so that errors can be seen in the docker log.
logging.basicConfig(level=logging.INFO)

# Get the date & time
# Split it out into date and time seperately, setting their format too
date_and_time = datetime.now()
current_time = date_and_time.strftime("%H:%M")
date = date_and_time.strftime("%d/%m/%Y")

# MQTT broker configuration 
mqtt_Broker = 'mqtt.em-solutions.co.uk' # Public IP of broker to connect to.
mqtt_Port = 1885 # Non-standard port for security.
mqtt_ClientID = "SmartMeterServer100084" # Set the server ClientID

# MQTT message topic configuration
mqtt_Topic = f'Clients/#' # Subscribe to all topics under "Clients/"
mqtt_ResponseTopic = f'Clients/{client_ID}/Response' # Set the topic that messages are recieved on. Also subscribe to all clients
mqtt_ErrorTopic = f'Clients/{client_ID}/Error' # Set the topic where error messages are sent to

# Output the client id to the log
#logging.info(f"Client ID: {client_ID}")

# Function to handle received messages
def on_message(client, userdata, message):
    # Check if message is not from response or error topics
    if not message.topic.endswith("/Response") and not message.topic.endswith("/Error"):
        received_message = json.loads(message.payload.decode()) # Decode the message received

        client_ID = received_message.get("Client ID")
        timestamp = received_message.get("Timestamp")
        power_Consumed = received_message.get("Power Consumed")

        if client_ID and timestamp and power_Consumed:
            # Calculate bill
            bill_Total = calculate_bill(power_Consumed)

            # Create or update CSV file and send response message
            update_csv(client_ID, timestamp, power_Consumed, bill_Total)
            publish_message(client, client_ID, bill_Total)
        else:
            logging.warning(f"Invalid message format: {message.topic}")

# The function that handles receiving outputting the price from the server
def calculate_bill (power_Consumed):
    bill_Total = float(power_Consumed)*1.843
    # Calculate the bill based on the power consumed 
    return bill_Total

def update_csv(client_ID, timestamp, power_Consumed, bill_Total):
    # Add csv logic here
    pass

def publish_message(client, client_ID, bill_Total):
    response_topic = f"Clients/{client_ID}/Response"
    message = {
        "Client ID": client_ID,
        "Message Topic": response_topic,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Bill Total": f"£{bill_Total:.2f}" # Format bill total with two decimal places
    }
    client.publish(response_topic, json.dumps(message))
    logging.info(f"Published response to {response_topic}")

def get_date (days_ago):
    today = datetime.now()
    target_date = today - timedelta(days=days_ago)
    return target_date.strftime("%d/%m/%Y")

def get_error (error_num):
    return "#" + str(error_num) + " Error "
    #datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_status (boolean):
    if boolean == True:
        return "ONLINE"
    else:
        return "OFFLINE"

def send_Report():
    # Define the message content
    message = {
        "Error": True,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Message": "There is an issue with the power grid. Contact your supplier."
    }

    # Publish the message to the designated topic
    client.publish(f"Clients/#", json.dumps(message)) # Publish to all clients
    logging.info(f"Published report message to Clients/#")

class errorLog_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # List to store timestamps
        self.timestamps = []

        # Widgets
        self.errorLabel1 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222")
        self.errorLabel1.grid(row=0, column=0, padx=20, pady=(8), sticky="nw")
        
        self.errorLabel2 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222")
        self.errorLabel2.grid(row=1, column=0, padx=20, pady=(8), sticky="nw")

        self.errorLabel3 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222")
        self.errorLabel3.grid(row=2, column=0, padx=20, pady=(8), sticky="nw")
        
        self.errorLabel4 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222")
        self.errorLabel4.grid(row=3, column=0, padx=20, pady=(8), sticky="nw")

        self.errorLabel5 = customtkinter.CTkLabel(self, font=("Consolas" ,11), text_color="#FF2222")
        self.errorLabel5.grid(row=4, column=0, padx=20, pady=(8), sticky="nw")

class userCard_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.loggedInLabel = customtkinter.CTkLabel(
            self,
            font=("Consolas", 10),
            text_color="#A3A3A3",
            text="You are logged in as:",
            anchor="w"
        )
        self.loggedInLabel.grid(row=0, column=0, padx=20, pady=(15,0), sticky="nsew")

        self.nameLabel = customtkinter.CTkLabel(
            self,
            font=("Consolas", 14),
            text_color="#FFFFF0",
            text=user,
            anchor="w"
        )
        self.nameLabel.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="nsew")

        #self.profilePicture = customtkinter.CTkImage("Icon2.ico")
        #self.profilePicture.grid(row=0, column=1, padx=20, pady=(15,0), sticky="e")

class status_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.statusLabel = customtkinter.CTkLabel(
            self,
            font=("Consolas", 12),
            text_color="#FFFFF0",
            text="Powergrid Status: " + get_status(status),
            anchor="w"
        )
        self.statusLabel.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")

        self.update_status()

    def update_status(self):
        self.statusLabel.configure(text="Powergrid Status: " + get_status(status))
        self.after(1000, self.update_status)

class button_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.reportButton = customtkinter.CTkButton(
            self,
            text="Report Issue",
            font=("Consolas", 12),
            text_color="#FFFFF0",
            command=self.report_click
        )
        self.reportButton.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")

        self.update_status()

    def report_click (self):
        # Get current timestamp
        global status
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Access errorLog object
        error_Log = self.master.errorLog
    
        # Update error labels with timestamps
        if len(error_Log.timestamps) < 5:
            error_Log.timestamps.append(current_time)
            label = getattr(error_Log, f"errorLabel{len(error_Log.timestamps)}")
            label.configure(text=f"{get_error(len(error_Log.timestamps))}{current_time}")
        elif len(error_Log.timestamps) == 5:
            # Overwrite oldest timestamp
            error_Log.timestamps.pop(0)
            error_Log.timestamps.append(current_time)
            #self.errorLabel.configure(text=f"{get_error(1)}{current_time}")

        if status == True:
            status = False
        else:
            status = True

    def get_button_text(self):
        if status == True:
            return "Report Issue"
        else:
            return "Report Fixed"
        
    def update_status(self):
        self.reportButton.configure(text=self.get_button_text())
        self.after(1000, self.update_status)

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("616x254")
        self.title("Smart Meter: Admin")
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.resizable(False, False)

        self.errorLog = errorLog_Frame(self)
        self.errorLog.grid(row=0, column=0, rowspan=3, padx=10, pady=(10), sticky="nsew")

        self.userCard = userCard_Frame(self)
        self.userCard.grid(row=0, column=1, padx=(0,10), pady=(10,10), sticky="nsew")

        self.statusWidget = status_Frame(self)
        self.statusWidget.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky="nsew")

        self.buttonWidget = button_Frame(self)
        self.buttonWidget.grid(row=2, column=1, padx=(0,10), pady=(0,10), sticky="nsew")


    # Add Methods to app
    def button_callback(self):
        print("Text output")

def mqtt_thread():
    # Set the on_message callback
    client = mqtt_client.Client(client_id=mqtt_ClientID, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    client.on_message = on_message

    # Connect to the broker
    client.connect(mqtt_Broker, mqtt_Port)

    # Subscribe to the topic to receive messages
    client.subscribe(mqtt_Topic)
    client.subscribe(mqtt_ErrorTopic)

    # Start the network loop to enable message reception
    client.loop_forever() # Start a networking daemon

# Create and start the MQTT thread
mqtt_thread = threading.Thread(target=mqtt_thread)
mqtt_thread.start()

# Create and start the main window
mainWindow = mainWindow()
mainWindow.mainloop()
>>>>>>> 09ec160 (Finalised the code.)
