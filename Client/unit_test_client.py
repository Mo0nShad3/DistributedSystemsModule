import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json

#import client
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import Client

class TestClientGeneration(unittest.TestCase):
    #Mock MQTT client instance
    @patch('Client.mqtt_client.Client')
    def test_generate_reading(self, MockMqttClient):
        
        mock_client_instance = MockMqttClient.return_value
        mock_client_instance.publish = MagicMock()
        
        #Gererate random values for testing
        with patch('random.uniform', return_value=5.0), patch('random.randint', return_value=30):
            with patch('datetime.datetime.now') as mock_now:
                mock_now.return_value.strftime.return_value = '2024-11-26 10:00:00'
                
                #Simulate reading generation
                Client.main_loop() 
                
                #Verify the JSON message + parameters
                expected_message = {
                    'Client ID': 'Client_1',
                    'Message Topic': 'Clients/Client_1',
                    'Timestamp': '2024-11-25 09:00:00',
                    'Power Consumed': '5.0',
                    'Publish Frequency': 30,
                    'Bool': True
                }
                mock_client_instance.publish.assert_called_with('Clients/Client_1', unittest.mock.ANY)
                
                # Get the actual arguments passed to the publish function
                args, kwargs = mock_client_instance.publish.call_args
                actual_message = json.loads(args[1])

                #Verify message contents can be generated and verified
                self.assertEqual(actual_message['Client ID'], 'Client_1')
                self.assertEqual(actual_message['Power Consumed'], '5.0')
                self.assertEqual(actual_message['Publish Frequency'], 30)

if __name__ == '__main__':
 unittest.main()
