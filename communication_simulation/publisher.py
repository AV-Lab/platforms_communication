from paho.mqtt import client as mqtt_client
from dotenv import load_dotenv
import os
import time
import random

# Load environment variables
load_dotenv()

# MQTT broker connection details
broker = os.getenv('MQTT_ADDR')
port = int(os.getenv('MQTT_PORT'))
username = os.getenv('MQTT_USER')
password = os.getenv('MQTT_PASS')

# Get client ID
client_id = input('Enter Client ID: ')
topic = input('Enter Topic to Publish: ')

def connect_mqtt():
    # Operations on connection
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connection is successful to broker...')
        else:
            print('Failed to connect to broker, return code %d\n', rc)
    # Set client ID (can be anything)
    client = mqtt_client.Client(client_id)
    # Set CA certificate
    client.tls_set(ca_certs='./certificates/emqxsl-ca.crt')
    # Set credentials
    client.username_pw_set(username, password)
    # Set on_connect function
    client.on_connect = on_connect
    # Connect to broker
    client.connect(broker, port)
    return client

def publish(client):
    while True:
        time.sleep(1)
        # Send a random int as speed for testing purposes
        msg = '{"speed": ' + str(random.randint(0, 40)) + '}'
        # Publish the message to topic
        result = client.publish(topic, msg)
        # Get status
        status = result[0]
        
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
    
