import sys
import serial as conn
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_21_InterfazConexion.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnAccion.clicked.connect(self.accion)
        self.arduino = None


    # Área de los Slots
    def accion(self):
        try:
            btnTexto = self.btnAccion.text()
            if btnTexto == "Conectar" and self.arduino is None:
                self.btnAccion.setText("Desconectar")
                self.arduino = conn.Serial(port=self.txtCOM.text(), baudrate=9600, timeout=10)
            elif btnTexto == "Desconectar" and self.arduino.is_open:
                self.arduino.close()
                self.btnAccion.setText("Reconectar")
            else:
                self.arduino.open()
                self.btnAccion.setText("Desconectar")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

