import paho.mqtt.client as mqtt
from Data import *
import time, json, base64

# This is the Subscriber
class subscriber():

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("incubator1")
        # client.subscribe("img1")          #test receiving image through MQTT

    def on_message(client, userdata, msg):
        if len(msg.payload) > 1:
            ud = Data()
            if msg.topic!='img1':
                data = msg.payload.decode()
                j = json.loads(data)
                ud.updateData(j)
                print str(data)
            else:       #test receiving image through MQTT
                print 'enter img1'
                data = msg.payload
                Data.img = base64.b64decode(data)
                print len(Data.img)
            time.sleep(1)

    client = mqtt.Client()
    client.connect("0.0.0.0", 1883, 60)

    client.on_connect = on_connect
    client.on_message = on_message

    def start(self):
        self.client.loop_forever()

    def stop(self):
        self.client.disconnect()


