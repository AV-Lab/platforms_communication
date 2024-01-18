from paho.mqtt import client as mqtt_client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MQTT broker connection details
broker = os.getenv('MQTT_ADDR')
port = int(os.getenv('MQTT_PORT'))
username = os.getenv('MQTT_USER')
password = os.getenv('MQTT_PASS')

# Get client ID
client_id = input('Enter Client ID: ')
topic = input('Enter Topic to Subscribe: ')

def connect_mqtt():
    # Operations on connection
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connection is successful to broker...')
        else:
            print('Failed to connect to broker, return code %d\n', rc)
    # Operations on message received
    def on_message(client, userdata, msg):
        print(msg.topic + ": " + str(msg.payload))
    # Set client ID (can be anything)
    client = mqtt_client.Client(client_id)
    # Set CA certificate
    client.tls_set(ca_certs='./certificates/emqxsl-ca.crt')
    # Set credentials
    client.username_pw_set(username, password)
    # Set on_connect function
    client.on_connect = on_connect
    # Set on_message function
    client.on_message = on_message
    # Connect to broker
    client.connect(broker, port)
    return client

def run():
    client = connect_mqtt()
    client.subscribe(topic)
    client.loop_forever()

if __name__ == '__main__':
    run()

