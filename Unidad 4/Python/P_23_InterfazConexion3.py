import sys
import serial as conn
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P_23_InterfazConexion3.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnAccion.clicked.connect(self.accion)
        self.arduino = None
        self.secondPlane = QtCore.QTimer()
        self.secondPlane.timeout.connect(self.lecturaDatos)
        self.btnLED.clicked.connect(self.ledControl)
        self.ledStatus = -1


    # Área de los Slots
    def accion(self):
        btnTexto = self.btnAccion.text()
        if btnTexto == "Conectar" and self.arduino is None:
            self.btnAccion.setText("Desconectar")
            self.arduino = conn.Serial(port=self.txtCOM.text(), baudrate=9600, timeout=1)
            self.secondPlane.start(100)
            print("conectao")
        elif btnTexto == "Desconectar" and self.arduino.is_open:
            self.secondPlane.stop()
            self.arduino.close()
            self.btnAccion.setText("Reconectar")
            print("desconectao")
        else:
            self.arduino.open()
            self.secondPlane.start(100)
            self.btnAccion.setText("Desconectar")
            print("conectao")

    def lecturaDatos(self):
        if self.arduino is not None and self.arduino.is_open:
            if self.arduino.inWaiting():
                cadena = self.arduino.readline()
                cadena = cadena.decode("utf-8").strip()
                print(cadena)
                if cadena != "":
                    self.listDatos.addItem(cadena)
                    self.listDatos.setCurrentRow(self.listDatos.rowCount())


    def ledControl(self):
        if self.arduino is not None and self.arduino.is_open:
            try:
                if self.ledStatus == -1:
                    self.btnLED.setText("Apagar")
                else:
                    self.btnLED.setText("Encender")
                val = "1" if self.ledStatus == 1 else "0" + '\n'
                self.arduino.write(val.encode())
                self.ledStatus = self.ledStatus * -1
            except Exception as e:
                print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

