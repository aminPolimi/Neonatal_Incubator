import threading, time, os
from DHT22 import DHT22Data
from Data import Data
import socket, json
import picamera
import RPi.GPIO as GPIO
import io

file = open("config","r")
serverIP = file.readline().replace('server=','')
os.system("sudo pigpiod")

clsData = Data()

def GetHumid_Temp():
    res = (1,1)
    while 1:
        res = DHT22Data(4)
        if int(res[0]) >= 0 and int(res[1] >=0 ):
            [clsData.humid, clsData.temp] = int(res[0]),int(res[1])
            print "produce    Temp: "+str(clsData.temp) + " , Humidity: "+str(clsData.humid)
            time.sleep(0.2)


<<<<<<< HEAD
def SendData():
    time.sleep(3)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverIP, 8002))
=======
def SendData(ip, port, bufferSize):
>>>>>>> origin/master
    while 1:
        message = dict()
        message["incID"] = clsData.incID  # incubator ID
        message["Humid"] = clsData.humid
        message["Temp"] = clsData.temp
        message["Lum"] = clsData.lum
        try:
            s.send(str(json.dumps(message)))
            #res = s.recv(16)
            print "send      "+str(message)
        except:
            print 'connection is closed'
        WriteLog(str(message))
        time.sleep(2)
    s.close()

def RecordCamera():
    client_socket = socket.socket()
    client_socket.connect((serverIP, 8001))
    connection = client_socket.makefile('wb')
    while 1:
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
            print 'connection is closed'

    connection.close()
    client_socket.close()


def WriteLog(message): # log data
    with open('log', 'a+') as f:
        f.write(message + "\n")


if __name__ == "__main__":
<<<<<<< HEAD
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)   # Humidity/Temperature sensor is connected to gpio 4

    thCamera = threading.Thread(target=RecordCamera)
    thCamera.start()
=======
    file = open("config","r")
    serverIP = file.readline()
    # thHT = threading.Thread(target=GetHumid_Temp)
    # thHT.start()
    thIP = threading.Thread(target=SendData(serverIP.replace("server=",""), 5005, 1024))
>>>>>>> origin/master

    thHT = threading.Thread(target=GetHumid_Temp)
    thHT.start()

    thData = threading.Thread(target=SendData)
    thData.start()

