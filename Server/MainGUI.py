# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import pyqtgraph as pg


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(971, 699)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(2, 16, 968, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grdLay1 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.grdLay1.setContentsMargins(0, 0, 0, 0)
        self.grdLay1.setObjectName("grdLay1")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 1, 71, 21))
        self.label.setObjectName("label")
        self.label.setText("Incubator 1")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 177, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Incubator 2")
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(2, 192, 968, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grdLay2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.grdLay2.setContentsMargins(0, 0, 0, 0)
        self.grdLay2.setObjectName("grdLay2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 353, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Incubator 3")
        self.gridLayoutWidget_3 = QtGui.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(2, 367, 968, 161))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.grdLay3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.grdLay3.setContentsMargins(0, 0, 0, 0)
        self.grdLay3.setObjectName("grdLay3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 530, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Incubator 4")
        self.gridLayoutWidget_4 = QtGui.QWidget(Form)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(2, 544, 968, 161))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.grdLay4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.grdLay4.setContentsMargins(0, 0, 0, 0)
        self.grdLay4.setObjectName("grdLay4")

        # QtCore.QObject.connect(self,QtCore.Signal("close()"),Form.)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # neonatal incubator 1
        self.plotTemp1 = pg.PlotWidget()
        self.plotTemp1.setTitle('Temprature')
        self.plotTemp1.setLabel('left', 'amplitude', 'V')
        self.plotTemp1.setLabel('bottom', 'time', 's')
        self.grdLay1.addWidget(self.plotTemp1, 1, 0)


        self.plotHumid1 = pg.PlotWidget()
        self.plotHumid1.setTitle('Humidity')
        self.plotHumid1.setLabel('left', 'amplitude', 'V')
        self.plotHumid1.setLabel('bottom', 'time', 's')
        self.grdLay1.addWidget(self.plotHumid1, 1, 1)

        self.plotLum1 = pg.PlotWidget()
        self.plotLum1.setTitle('Luminosity')
        self.plotLum1.setLabel('left', 'amplitude', 'V')
        self.plotLum1.setLabel('bottom', 'time', 's')
        self.grdLay1.addWidget(self.plotLum1, 1, 2)

        # neonatal incubator 2
        self.plotTemp2 = pg.PlotWidget()
        self.plotTemp2.setTitle('Temprature')
        self.plotTemp2.setLabel('left', 'amplitude', 'V')
        self.plotTemp2.setLabel('bottom', 'time', 's')
        self.grdLay2.addWidget(self.plotTemp2, 2, 0)

        self.plotHumid2 = pg.PlotWidget()
        self.plotHumid2.setTitle('Humidity')
        self.plotHumid2.setLabel('left', 'amplitude', 'V')
        self.plotHumid2.setLabel('bottom', 'time', 's')
        self.grdLay2.addWidget(self.plotHumid2, 2, 1)

        self.plotLum2 = pg.PlotWidget()
        self.plotLum2.setTitle('Luminosity')
        self.plotLum2.setLabel('left', 'amplitude', 'V')
        self.plotLum2.setLabel('bottom', 'time', 's')
        self.grdLay2.addWidget(self.plotLum2, 2, 2)

        # neonatal incubator 3
        self.plotTemp3 = pg.PlotWidget()
        self.plotTemp3.setTitle('Temprature')
        self.plotTemp3.setLabel('left', 'amplitude', 'V')
        self.plotTemp3.setLabel('bottom', 'time', 's')
        self.grdLay3.addWidget(self.plotTemp3, 3, 0)

        self.plotHumid3 = pg.PlotWidget()
        self.plotHumid3.setTitle('Humidity')
        self.plotHumid3.setLabel('left', 'amplitude', 'V')
        self.plotHumid3.setLabel('bottom', 'time', 's')
        self.grdLay3.addWidget(self.plotHumid3, 3, 1)

        self.plotLum3 = pg.PlotWidget()
        self.plotLum3.setTitle('Luminosity')
        self.plotLum3.setLabel('left', 'amplitude', 'V')
        self.plotLum3.setLabel('bottom', 'time', 's')
        self.grdLay3.addWidget(self.plotLum3, 3, 2)

        # neonatal incubator 4
        self.plotTemp4 = pg.PlotWidget()
        self.plotTemp4.setTitle('Temprature')
        self.plotTemp4.setLabel('left', 'amplitude', 'V')
        self.plotTemp4.setLabel('bottom', 'time', 's')
        self.grdLay4.addWidget(self.plotTemp4, 4, 0)

        self.plotHumid4 = pg.PlotWidget()
        self.plotHumid4.setTitle('Humidity')
        self.plotHumid4.setLabel('left', 'amplitude', 'V')
        self.plotHumid4.setLabel('bottom', 'time', 's')
        self.grdLay4.addWidget(self.plotHumid4, 4, 1)

        self.plotLum4 = pg.PlotWidget()
        self.plotLum4.setTitle('Luminosity')
        self.plotLum4.setLabel('left', 'amplitude', 'V')
        self.plotLum4.setLabel('bottom', 'time', 's')
        self.grdLay4.addWidget(self.plotLum4, 4, 2)

        # self.lblImage = QtGui.QLabel()          #test receiving image through MQTT
        # self.grdLay4.addWidget(self.lblImage,4,2)   #test receiving image through MQTT


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

