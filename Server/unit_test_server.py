import unittest
from unittest.mock import MagicMock, patch
import json
import paho.mqtt.client as mqtt_client
#import server file
from ServerUnitTest import on_connect, on_message, create_mqtt_client

class TestServer(unittest.TestCase):

    @patch('paho.mqtt.client.Client')
    def setUp(self, MockMqttClient):
        #Mock MQTT client instance
        self.mock_client = MagicMock()
        #Mock connection
        self.mock_client.subscribe = MagicMock()
        self.mock_client.publish = MagicMock()
        self.mock_client.connect = MagicMock()
        self.mock_client.on_connect = on_connect
        self.mock_client.on_message = on_message

        #Simulate a callback on connection
        self.mock_client.on_connect(self.mock_client, None, None, 0, None)

    def test_on_connect(self):
        #Test the on_connect callback + Check the subscribtion topic is called
        self.mock_client.on_connect(self.mock_client, None, None, 0, None)
        self.mock_client.subscribe.assert_called_with("Clients/Client_1")

    @patch('random.uniform')
    def test_on_message_valid(self, mock_uniform):
        #Mocking  random.uniform for a 'fixed bill total' value
        mock_uniform.return_value = 500.0

        #Simulate a message
        test_message = {
            "Client ID": "Client_1",
            "Message Topic": "Clients/Client_1",
            "Timestamp": "2024-11-26 12:34:56",
            "Power Consumed": "3.5", 
            "Publish Frequency": "30",
            "Bool": True
        }

        #Simulate message callback
        mock_message = MagicMock()
        mock_message.payload = json.dumps(test_message).encode()
        mock_message.topic = "Clients/Client_1"

        on_message(self.mock_client, None, mock_message)

        #Create response
        expected_message = {
            "Client ID": "Client_1",
            "Message Topic": "Clients/Client_1",
            "Timestamp": "2024-11-26 12:34:56",
            "Power Consumed": "3.5",
            "Publish Frequency": "30",
            "Bool": True,
            "Bill Total": 500.0
        }

        #Verify the expected message
        self.mock_client.publish.assert_called_with("Clients/Client_1/Response", json.dumps(expected_message))

if __name__ == '__main__':
    unittest.main()
