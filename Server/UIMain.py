from PySide import QtGui, QtCore
from MainGUI import Ui_Form
from Data import Data
import threading, time, socket, json, subprocess
from random import randint

class clsMain(QtGui.QWidget):

    thIP = threading.Thread
    closedForm = False
    def __init__(self, parent=None):
        super(clsMain, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # repetitive and single-shot timer   -> Thread
        # we use this timer when QtGui is used into function
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refreshChart)
        self.timer.start(2000)  # 1 second

        thIP = threading.Thread(target = self.listenIP)
        thIP.start()

        thCamera = threading.Thread(target = self.loadCamera)
        thCamera.start()
        # print 'load camera'

    ##---------------------------------------------------
    def closeEvent(self, event):
        print 'close'
        self.closedForm = True

    ##---------------------------------------------------
    def updateData(self, jData):
        if jData["incID"] == 1:
            if len(Data.inc1["Temp"][1]) == Data.quLength:
                del Data.inc1["Temp"][1][0] , Data.inc1["Humid"][1][0], Data.inc1["Lum"][1][0]
            else:
                inc1Num = int(len(Data.inc1["Temp"][0]) + 1)
                Data.inc1["Temp"][0].append(inc1Num) , Data.inc1["Humid"][0].append(inc1Num)
                Data.inc1["Lum"].append(inc1Num)

            Data.inc1["Temp"][1].append(int(jData["Temp"]))
            Data.inc1["Humid"][1].append(int(jData["Humid"])), Data.inc1["Lum"][1].append(int(jData["Lum"]))
        # elif data["incID"] == 2:
        #     if len(Data.inc2["Temp"][1]) == Data.quLength:
        #         del Data.inc2["Temp"][1][0] , Data.inc2["Humid"][1][0], Data.inc2["Lum"][1][0]
        #     else:
        #         inc1Num = len(Data.inc1["Temp"][0]) + 1
        #         Data.inc1["Temp"][0].append(inc1Num) , Data.inc1["Humid"][0].append(inc1Num)
        #         Data.inc1["Lum"].append(inc1Num)
        #     Data.inc2["Temp"][1].append(data["temp"])
        #     Data.inc2["Humid"][1].append(data["humid"]), Data.inc2["Lum"][1].append(data["lum"])
        # elif data["incID"] == 3:
        #     if len(Data.inc3["Temp"][1]) == Data.quLength:
        #         del Data.inc3["Temp"][1][0] , Data.inc3["Humid"][1][0], Data.inc3["Lum"][1][0]
        #     else:
        #         inc1Num = len(Data.inc1["Temp"][0]) + 1
        #         Data.inc1["Temp"][0].append(inc1Num) , Data.inc1["Humid"][0].append(inc1Num)
        #         Data.inc1["Lum"].append(inc1Num)
        #     Data.inc3["Temp"][1].append(data["temp"])
        #     Data.inc3["Humid"][1].append(data["humid"]), Data.inc3["Lum"][1].append(data["lum"])
        # elif data["incID"] == 4:
        #     if len(Data.inc4["Temp"][1]) == Data.quLength:
        #         del Data.inc4["Temp"][1][0] , Data.inc4["Humid"][1][0], Data.inc4["Lum"][1][0]
        #     else:
        #         inc1Num = len(Data.inc1["Temp"][0]) + 1
        #         Data.inc1["Temp"][0].append(inc1Num) , Data.inc1["Humid"][0].append(inc1Num)
        #         Data.inc1["Lum"].append(inc1Num)
        #     Data.inc4["Temp"][1].append(data["temp"])
        #     Data.inc4["Humid"][1].append(data["humid"]), Data.inc4["Lum"][1].append(data["lum"])

    ##---------------------------------------------------
    def listenIP(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 8002))
        s.listen(1)
        conn, addr = s.accept()
        while not self.closedForm:
            data = conn.recv(1024)
            conn.send("test resp")  # echo
            print data
            if len(data)>5:
                j = json.loads(data)
                self.updateData(j)
            time.sleep(2)

            if not data: break



    def loadCamera(self):
        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8001))
        server_socket.listen(0)
        connection = server_socket.accept()[0].makefile('rb')
        try:
            # Run a viewer with an appropriate command line. Uncomment the mplayer
            # version if you would prefer to use mplayer instead of VLC
            # cmdline = ['/Applications/VLC.app/Contents/MacOS/cvlc', '--demux', 'h264', '-']
            cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
            player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
            while True:
                # Repeatedly read 1k of data from the connection and write it to
                # the media player's stdin
                data = connection.read(1024)
                if not data:
                    break
                player.stdin.write(data)
        finally:
            connection.close()
            server_socket.close()
            player.terminate()




    ##---------------------------------------------------
    def refreshChart(self):
        if len(Data.inc1["Temp"][0])>0:
            self.ui.plotTemp1.clear()
            self.ui.plotTemp1.plot(Data.inc1["Temp"][0], Data.inc1["Temp"][1])
            self.ui.plotHumid1.clear()
            self.ui.plotHumid1.plot(Data.inc1["Humid"][0], Data.inc1["Humid"][1])
            # self.ui.plotLum1.clear()
            # self.ui.plotLum1.plot(Data.inc1["Lum"][0], Data.inc1["Lum"][1])
        #
        # self.ui.plotTemp2.clear()
        # self.ui.plotTemp2.plot(Data.inc2["Temp"][0], Data.inc2["Temp"][1])
        # self.ui.plotHumid2.clear()
        # self.ui.plotHumid2.plot(Data.inc2["Humid"][0], Data.inc2["Humid"][1])
        # self.ui.plotLum2.clear()
        # self.ui.plotLum2.plot(Data.inc2["Lum"][0], Data.inc2["Lum"][1])
        #
        # self.ui.plotTemp3.clear()
        # self.ui.plotTemp3.plot(Data.inc3["Temp"][0], Data.inc3["Temp"][1])
        # self.ui.plotHumid3.clear()
        # self.ui.plotHumid3.plot(Data.inc3["Humid"][0], Data.inc3["Humid"][1])
        # self.ui.plotLum3.clear()
        # self.ui.plotLum3.plot(Data.inc3["Lum"][0], Data.inc3["Lum"][1])
        #
        # self.ui.plotTemp4.clear()
        # self.ui.plotTemp4.plot(Data.inc4["Temp"][0], Data.inc4["Temp"][1])
        # self.ui.plotHumid4.clear()
        # self.ui.plotHumid4.plot(Data.inc1["Humid"][0], Data.inc1["Humid"][1])
        # self.ui.plotLum4.clear()
        # self.ui.plotLum4.plot(Data.inc4["Lum"][0], Data.inc4["Lum"][1])


