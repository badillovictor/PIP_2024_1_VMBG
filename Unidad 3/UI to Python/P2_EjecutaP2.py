import sys
import P2_Ejemplo as interfaz
from PyQt5 import uic, QtWidgets, QtCore
#qtCreatorFile = "P1_Ejemplo.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnNuevo = QtWidgets.QPushButton(self.centralwidget)
        self.btnNuevo.setGeometry(QtCore.QRect(380, 180, 200, 70))
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnNuevo.setText("Me cree")

        # Área de los Signals
        self.btnSaludar.clicked.connect(self.saludar)
        self.btnNuevo.clicked.connect(self.saludar)

    # Área de los Slots
    def saludar(self):
        if self.sender() == self.btnSaludar:
            self.txtValor.setText("Saludo viejo")
        if self.sender() == self.btnNuevo:
            self.txtValor.setText("Saludo nuevo")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

