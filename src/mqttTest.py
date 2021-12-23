import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

brokerAddress = "192.168.1.12"
#brokerAddress = "localhost"
#client.connect("mqtt.eclipseprojects.io", 1883, 60)
broker = client.connect(brokerAddress, 1883, 60)

print('broker:', broker)

topic = 'classroom/pythonscript'
msg = 'works from python'
result = client.publish(topic, msg)
# result[0] is status, 0 is good, 1 is error

print('result:', result)
