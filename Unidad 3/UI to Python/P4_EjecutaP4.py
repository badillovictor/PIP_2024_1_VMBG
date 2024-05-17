import sys
import P3_ComunicacionVentanas as interfaz
from P4_EjecutaP4Dialog import MyDialog
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P4_ComunicacionVentanas2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        # Área de los Signals
        self.btnMandarSumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        try:
            self.dialog = MyDialog(self)
            self.dialog.setModal(True)
            self.dialog.show()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

