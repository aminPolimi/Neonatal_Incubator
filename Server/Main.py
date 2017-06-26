import sys
from PySide import QtCore, QtGui, QtUiTools
from UIMain import clsMain
from Data import Data

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    frmMain = clsMain()
    frmMain.show()
    sys.exit(app.exec_())




