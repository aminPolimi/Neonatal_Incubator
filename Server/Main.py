import sys
from PySide import QtCore, QtGui, QtUiTools
from UIMain import clsMain
from Data import Data



def getIpData():
    if len(Data.inc1["Temp"][1]) == Data.quLength:
        del Data.inc1["Temp"][1][0]#, Data.inc1["Humid"][1][0], Data.inc1["Lum"][1][0]
    Data.inc1["Temp"][1].append(10), Data.inc1["Humid"][1].append(12), Data.inc1["Lum"][1].append(13)

    # if len(Data.inc2["Temp"][1]) == Data.quLength:
    #     del Data.inc2["Temp"][1][0], Data.inc2["Humid"][1][0]
    # GraphDL.chart2["Temp"][1].append(temp), GraphDL.chart2["Humid"][1].append(humid)

# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return "Hello, World!" + str(Data.quLength)
#
#
# def webSrv():
#     app.run(debug=True)
#
# p = multiprocessing.Process(target=webSrv)

if __name__ == "__main__":

    # thIP = threading.Thread(target=webSrv)
    # p.start()
    #getIpData()
    app = QtGui.QApplication(sys.argv)
    frmMain = clsMain()
    frmMain.show()
    sys.exit(app.exec_())

    # import socket
    #
    # TCP_IP = '10.169.195.140'
    # TCP_PORT = 5005
    # BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    #
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind((TCP_IP, TCP_PORT))
    # s.listen(1)
    #
    # conn, addr = s.accept()
    #
    # #conn.close()
    # print 'Connection address:', addr
    # while 1:
    #     data = conn.recv(BUFFER_SIZE)
    #     if not data: break
    #     print "received data:", data
    #     #conn.send(data)  # echo
    # conn.close()




