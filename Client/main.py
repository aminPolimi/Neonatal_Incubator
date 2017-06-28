import threading, time, os
from DHT22 import DHT22Data
from Data import Data
import socket, json, io, base64
import picamera
import RPi.GPIO as GPIO
from TSL2561 import tsl2561
import paho.mqtt.client as mqtt
#from PIL import Image

file = open("config","r")
serverIP = file.readline().replace('server=','')
os.system("sudo pigpiod")

clsData = Data()
runApp = True

client_socket = socket.socket()
client_socket.connect((serverIP, 8001))
connection = client_socket.makefile('wb')

stream = io.BytesIO()

def GetHumid_Temp():
    res = (1,1)
    while runApp:
        try:
            res = DHT22Data(10)
            if int(res[0]) >= 0 and int(res[1]) >=0 :
                [clsData.humid, clsData.temp] = int(res[0]),int(res[1])
                # print "produce    Temp: "+str(clsData.temp) + " , Humidity: "+str(clsData.humid)
        except:
            print 'error producing sensor data'
        finally:
            time.sleep(0.2)
#
def GetLuminasity():
    lum = tsl2561()
    while runApp:
        clsData.lum = lum.getTSL()
        #print clsData.lum
        time.sleep(1)
#
def SendData():
    time.sleep(3)
    client = mqtt.Client()
    client.connect(serverIP, 1883, 60)
    # i=0
    while runApp:
        message = dict()
        message["incID"] = clsData.incID  # incubator ID
        message["Humid"] = clsData.humid
        message["Temp"] = clsData.temp
        message["Lum"] = clsData.lum

        ## image = Image.open(stream.getvalue())
        ## out = io.BytesIO()
        ## # image.save(out, quality=20, optimize=True)
        ## image.save(stream, 'JPEG', dpi=[480, 360], quality=80)
        ## image.seek(0)
        ## #print len(out.getvalue())
        ## #print len(base64.b64decode(out.getvalue()))

        # stm64 = base64.b64encode(stream.getvalue())     #test sending image through MQTT

        try:
            client.publish("incubator1", str(json.dumps(message)));
            # client.publish("img1", stm64);            #test sending image through MQTT
            print "send:  "+str(message)
        except:
            pass
        WriteLog(str(message))
        time.sleep(2)
    client.disconnect();

def RecordCamera():

    while runApp:
        try:
            with picamera.PiCamera() as camera:
                camera.resolution = (640, 480)
                camera.framerate = 24
                # Start a preview and let the camera warm up for 2 seconds
                camera.start_preview()
                time.sleep(2)
                # Start recording, sending the output to the connection for 60
                # seconds, then stop
                camera.annotate_text = "Incubator " + str(Data.incID)
                camera.start_recording(connection, format='h264')
                camera.wait_recording(60)
                camera.stop_recording()
        finally:
            print 'camera connection is closed'


def WriteLog(message): # log data
    with open('log', 'a+') as f:
        f.write(message + "\n")



def TakePicture():      #test sending image through MQTT
    global stream
    while runApp:
        with picamera.PiCamera() as camera:
            camera.resolution = (480, 360)
            camera.start_preview()
            time.sleep(1)
            camera.capture(stream, format='jpeg', resize=(480, 360))
            # camera.capture('img.jpg', resize=(480, 360))
        # "Rewind" the stream to the beginning so we can read its content
        stream.seek(0)
        time.sleep(2)


if __name__ == "__main__":
    try:
        GPIO.cleanup()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(10, GPIO.OUT)   # Humidity/Temperature sensor is connected to gpio 10

        thCamera = threading.Thread(target=RecordCamera)    # use 'TakePicture' instead of 'RecordCamera' to test MQTT
        thCamera.start()

        thHT = threading.Thread(target=GetHumid_Temp)
        thHT.start()

        thLum = threading.Thread(target=GetLuminasity)
        thLum.start()

        thData = threading.Thread(target=SendData)
        thData.start()
    except KeyboardInterrupt:
        runApp = False
        os.system("sudo killall -9 python main.py")
        connection.close()
        client_socket.close()


