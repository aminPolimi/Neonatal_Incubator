import paho.mqtt.client as mqtt
from Data import *
import time, json

# This is the Subscriber
class subscriber():

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("incubator1")

    def on_message(client, userdata, msg):
        data = msg.payload.decode()
        if len(data) > 1:
            print str(data)
            j = json.loads(data)
            ud = Data()
            ud.updateData(j)
        time.sleep(1)

    client = mqtt.Client()
    client.connect("0.0.0.0", 1883, 60)

    client.on_connect = on_connect
    client.on_message = on_message

    def start(self):
        self.client.loop_forever()

    def stop(self):
        self.client.disconnect()


