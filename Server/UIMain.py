from PySide import QtGui, QtCore
from MainGUI import Ui_Form
from Data import Data
import threading, socket, subprocess
from Subscriber import *

class clsMain(QtGui.QWidget):

    thIP = threading.Thread
    closedForm = False
    s = subscriber()
    def __init__(self, parent=None):
        super(clsMain, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # repetitive and single-shot timer   -> Thread
        # we use this timer when QtGui is used into function
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refreshChart)
        self.timer.start(2000)  # 1 second

        thIP = threading.Thread(target = self.s.start)
        thIP.start()

        thCamera = threading.Thread(target = self.loadCamera)
        thCamera.start()

    ##---------------------------------------------------
    def closeEvent(self, event):
        print 'app closed'
        self.s.stop()
        self.closedForm = True

    ##---------------------------------------------------
    def loadCamera(self):
        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8001))
        server_socket.listen(0)
        connection = server_socket.accept()[0].makefile('rb')
        try:
            # Run a viewer with an appropriate command line. Uncomment the mplayer
            # version if you would prefer to use mplayer instead of VLC
            # cmdline = ['/Applications/VLC.app/Contents/MacOS/cvlc', '--demux', 'h264', '-']
            cmdline = ['mplayer', '-fps', '25',  '-']
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
            self.ui.plotLum1.clear()
            self.ui.plotLum1.plot(Data.inc1["Lum"][0], Data.inc1["Lum"][1])


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


