from PySide import QtGui, QtCore
from MainGUI import Ui_Form
from Data import Data
import threading, time
import numpy as np
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
        self.timer.start(2000)  # 5 seconds

        self.refreshChart()
        thIP = threading.Thread(target=self.listenIP)
        thIP.start()


    def closeEvent(self, event):
        # do stuff
        print 'close'
        self.closedForm = True


    def listenIP(self):
        while not self.closedForm:
            print 'ip'
            if len(Data.inc1["Temp"][1]) == Data.quLength:
                del Data.inc1["Temp"][1][0]  # , Data.inc1["Humid"][1][0], Data.inc1["Lum"][1][0]
            Data.inc1["Temp"][1].append(randint(0,9))#, Data.inc1["Humid"][1].append(12), Data.inc1["Lum"][1].append(13)

            time.sleep(2)

    def refreshChart(self):
        self.ui.plotTemp1.clear()
        self.ui.plotTemp1.plot(Data.inc1["Temp"][0], Data.inc1["Temp"][1])



        # dates = np.arange(8) * (3600 * 24 * 356)
        # self.ui.plotTemp1.plot(x=dates, y=[1, 6, 2, 4, 3, 5, 6, 8], symbol='o')

        # self.ui.plotHumid1.clear()
        # self.ui.plotHumid1.plot(Data.inc1["Humid"][0], Data.inc1["Humid"][1])
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


