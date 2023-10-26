import time 
import paho.mqtt.client as paho

broker = "broker.emqx.io"
client = paho.Client("client-isu-002")

print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
print("Publishing")

while True:
    state = input()
    client.publish("esp8266check/lipa", state)
    time.sleep(2)
    if state == "1":
        break

client.disconnect()
client.loop_stop()