import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog

qtCreatorFile = "P_07_CambiarColor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.R = 0
        self.G = 0
        self.B = 0
        self.txtR.setText(str(self.R))
        self.txtG.setText(str(self.G))
        self.txtB.setText(str(self.B))

        self.sliderR.setMinimum(0)
        self.sliderR.setMaximum(255)
        self.sliderR.setSingleStep(1)
        self.sliderR.setValue(0)
        self.sliderR.valueChanged.connect(self.setR)

        self.sliderG.setMinimum(0)
        self.sliderG.setMaximum(255)
        self.sliderG.setSingleStep(1)
        self.sliderG.setValue(0)
        self.sliderG.valueChanged.connect(self.setG)

        self.sliderB.setMinimum(0)
        self.sliderB.setMaximum(255)
        self.sliderB.setSingleStep(1)
        self.sliderB.setValue(0)
        self.sliderB.valueChanged.connect(self.setB)

    # Área de los Slots
    def setR(self):
        self.R = self.sliderR.value()
        estilo = ("background-color: rgb(" + str(self.R) +
                  "," + str(self.G) + "," + str(self.B) + ");")
        self.lbColor.setStyleSheet(estilo)
        self.txtR.setText(str(self.R))

    def setG(self):
        self.G = self.sliderG.value()
        estilo = ("background-color: rgb(" + str(self.R) +
                  "," + str(self.G) + "," + str(self.B) + ");")
        self.lbColor.setStyleSheet(estilo)
        self.txtG.setText(str(self.G))

    def setB(self):
        self.B = self.sliderB.value()
        estilo = ("background-color: rgb(" + str(self.R) +
                  "," + str(self.G) + "," + str(self.B) + ");")
        self.lbColor.setStyleSheet(estilo)
        self.txtB.setText(str(self.B))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
