import random
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpenAritmeticas.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnSumar.clicked.connect(self.sumar)
        self.btnRestar.clicked.connect(self.restar)
        self.btnMultiplicar.clicked.connect(self.multiplicar)
        self.btnDividir.clicked.connect(self.dividir)

    # Área de los Slots
    def sumar(self):
        suma = int(self.txtA.text()) + int(self.txtB.text())
        self.txtResultado.setText(str(suma))

    def restar(self):
        resta = int(self.txtA.text()) - int(self.txtB.text())
        self.txtResultado.setText(str(resta))

    def multiplicar(self):
        multiplicacion = int(self.txtA.text()) * int(self.txtB.text())
        self.txtResultado.setText(str(multiplicacion))

    def dividir(self):
        division = int(self.txtA.text()) / int(self.txtB.text())
        self.txtResultado.setText(str(division))

if __name__ == "__main__":
    print(random.randint(0, 1))
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

