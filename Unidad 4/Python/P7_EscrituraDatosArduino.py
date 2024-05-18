import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P7_EscrituraDatosArduino1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.btn_enviar.clicked.connect(self.enviar_dato)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaSerial)
        self.arduino = None

    #Area de Slots
    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
            self.arduino.close()
            self.segundoPlano.stop()
            self.btn_accion.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")

    def enviar_dato(self):
        if self.arduino is not None and self.arduino.isOpen():
            dato = self.txt_numero.text()
            self.arduino.write(dato.encode())
            print("envio dato")

    def lecturaSerial(self):
        if self.arduino is not None and self.arduino.isOpen():
            if self.arduino.inWaiting():
                print("Recibo dato")
                cadena = self.arduino.readline().decode().strip()
                if cadena:
                    print("Recibo dato")
                    self.txtRespuesta.setText(cadena)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())