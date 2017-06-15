import threading, time
# from DHT22 import DHT22Data
from Data import Data

def GetHumid_Temp():
    while 1 and Data.sent:
        # res = DHT22Data(16)
        # [Data.temp, Data.humid] = int(res[0]),int(res[1])
        # print "Temp: "+Data.temp + " , Humidity: "+Data.humid
        time.sleep(2)


def SendData(ip, port, bufferSize):
    while 1:
        message = '{ "temp":'+str(Data.temp)+', "humid":'+str(Data.humid)+', "light":'+str(0)+'}'
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((TCP_IP, TCP_PORT))
        # s.send(message)
        # s.close()
        print ip, port, bufferSize
        time.sleep(2)


if __name__ == "__main__":
    file = open("config","r")
    serverIP = file.readline()
    # thHT = threading.Thread(target=GetHumid_Temp)
    # thHT.start()
    thIP = threading.Thread(target=SendData(serverIP.replace("server=",""), 5005, 1024))



