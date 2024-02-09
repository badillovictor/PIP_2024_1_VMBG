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
        self.btnSumar.clicked.connect(self.calcular)
        self.btnRestar.clicked.connect(self.calcular)
        self.btnMultiplicar.clicked.connect(self.calcular)
        self.btnDividir.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        sender = self.sender().objectName()
        if sender == "btnSumar":
            suma = int(self.txtA.text()) + int(self.txtB.text())
            self.txtResultado.setText(str(suma))
        elif sender == "btnRestar":
            resta = int(self.txtA.text()) - int(self.txtB.text())
            self.txtResultado.setText(str(resta))
        elif sender == "btnMultiplicar":
            multiplicacion = int(self.txtA.text()) * int(self.txtB.text())
            self.txtResultado.setText(str(multiplicacion))
        elif sender == "btnDividir":
            division = int(self.txtA.text()) / int(self.txtB.text())
            self.txtResultado.setText(str(division))


if __name__ == "__main__":
    print(random.randint(0, 1))
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

