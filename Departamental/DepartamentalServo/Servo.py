import serial
import sys
from PyQt5 import uic, QtGui, QtWidgets, QtCore

qtCreatorFile = "Servo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnArduino.clicked.connect(self.conexionArduino)
        self.QtTimer = QtCore.QTimer()
        self.QtTimer.timeout.connect(self.lecturaArduino)
        self.QtTimer.setInterval(1000)
        self.conexion = -1
        self.arduino = None

    def conexionArduino(self):
        if self.conexion == -1:
            self.arduino = serial.Serial(port='com4', baudrate=9600, timeout=10)
            self.btnArduino.setText("Desconectar")
            self.conexion = 1
            self.QtTimer.start()
        if self.conexion == 0:
            self.arduino.open()
            self.btnArduino.setText("Desconectar")
            self.conexion = 1
            self.QtTimer.start()
        if self.conexion == 1:
            self.arduino.close()
            self.btnArduino.setText("Conectar")
            self.conexion = 0
            self.QtTimer.stop()

    def lecturaArduino(self):
        if self.arduino is not None and self.arduino.isOpen():
            lectura = self.arduino.readline().decode().strip()
            if lectura != "":
                self.lbMovimiento.setText(lectura)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
