import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_02_HelloInputText.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnSaludar.clicked.connect(self.saludar)

    # Área de los Slots
    def saludar(self):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText('Hello {0}, you are {1} years old'.format(self.txtNombre.text(), self.txtEdad.text()))
        messageBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

