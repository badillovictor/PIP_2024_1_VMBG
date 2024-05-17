import sys
import P3_ComunicacionVentanas as interfaz
from P3_EjecutaP3Dialog import MyDialog
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P3_ComunicacionVentanas.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dialog = MyDialog()

        # Área de los Signals
        self.btnSumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        try:
            a = int(self.txtValorA.text())
            b = int(self.txtValorB.text())
            res = a + b
            self.dialog.setModal(False)
            self.dialog.txtResultado.setText(str(res))
            self.dialog.show()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

