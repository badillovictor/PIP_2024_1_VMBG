import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_13_SeleccionEquipoV2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rbEduardo.toggled.connect(self.clickEduardo)
        self.rbSofia.toggled.connect(self.clickSofia)
        self.rbUriel.toggled.connect(self.clickUriel)
        self.rbVictor.toggled.connect(self.clickVictor)

    # Área de los Slots
    def clickEduardo(self):
        if self.rbEduardo.isChecked():
            self.txtPersona.setText("Eduardo")

    def clickUriel(self):
        if self.rbUriel.isChecked():
            self.txtPersona.setText("Uriel")

    def clickSofia(self):
        if self.rbSofia.isChecked():
            self.txtPersona.setText("Sofia")

    def clickVictor(self):
        if self.rbVictor.isChecked():
            self.txtPersona.setText("Victor")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
