import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P16_LM35.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.mostrar_temperaturas)

    #Area de Slots
    def accion(self):
        try:
            texto_boton = self.btn_accion.text()
            com = self.txt_com.text()
            if texto_boton == "CONECTAR" and self.arduino is None:
                self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
                self.btn_accion.setText("DESCONECTAR")
                self.segundoPlano.start(100)
            elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
                self.arduino.close()
                self.btn_accion.setText("RECONECTAR")
                self.segundoPlano.stop()
            else:
                self.arduino.open()
                self.btn_accion.setText("DESCONECTAR")
                self.segundoPlano.start(100)
        except Exception as e:
            print(e)

    def mostrar_temperaturas(self):
        if self.arduino and self.arduino.isOpen():
            # Leer la línea del puerto serial
            lectura = self.arduino.readline().decode().strip()
            print(lectura)
            valores = lectura.split(",")  # Separar los valores por la coma
            if len(valores) == 2:  # Asegurarse de que haya recibido dos valores
                # Asignar los valores a temp1 y temp2
                temp1 = valores[0]
                temp2 = valores[1]
                # Mostrar los valores en los QLineEdit
                self.txt_lm35.setText(temp1)
                self.txt_temperatura.setText(temp2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())