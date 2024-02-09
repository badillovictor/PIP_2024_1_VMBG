import random
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_06_Suma_V2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnSumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        numeros = self.txtNumeros.text()
        numeros = numeros.split(", ")
        suma = 0
        ## En lugar de convertir todos los numeros a int y despues sumarlos todos (2N porque recorre la lsita 2 veces)
        ## recorri la lsita solo una vez, convirtiendo a int y sumando al mismo tiempo (N)
        for num in numeros:
            suma += int(num)
        self.txtResultado.setText(str(suma))


if __name__ == "__main__":
    print(random.randint(0, 1))
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

