import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_06_Unidades.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.txtGramos.setInputMask('000000000')
        self.txtMetros.setInputMask('000000000')
        self.txtLitros.setInputMask('000000000')

        # Área de los Signals
        self.txtGramos.textEdited.connect(self.calculate)
        self.txtMetros.textEdited.connect(self.calculate)
        self.txtLitros.textEdited.connect(self.calculate)

    # Área de los Slots
    def calculate(self):
        try:
            sender = self.sender()
            if sender == self.txtMetros:
                base = self.txtMetros.text()
                if base.isnumeric():
                    self.txtDecaMetros.setText(str(self.calculateDeca(base)))
                    self.txtHectoMetros.setText(str(self.calculateHecto(base)))
                    self.txtKiloMetros.setText(str(self.calculateKilo(base)))
                    self.txtMegaMetros.setText(str(self.calculateMega(base)))
                    self.txtDeciMetros.setText(str(self.calculateDeci(base)))
                    self.txtCentiMetros.setText(str(self.calculateCenti(base)))
                    self.txtMiliMetros.setText(str(self.calculateMili(base)))
                    self.txtMicroMetros.setText(str(self.calculateMicro(base)))
                    self.txtNanoMetros.setText(str(self.calculateNano(base)))
            elif sender == self.txtGramos:
                base = self.txtGramos.text()
                if base.isnumeric():
                    self.txtDecaGramos.setText(str(self.calculateDeca(base)))
                    self.txtHectoGramos.setText(str(self.calculateHecto(base)))
                    self.txtKiloGramos.setText(str(self.calculateKilo(base)))
                    self.txtMegaGramos.setText(str(self.calculateMega(base)))
                    self.txtDeciGramos.setText(str(self.calculateDeci(base)))
                    self.txtCentiGramos.setText(str(self.calculateCenti(base)))
                    self.txtMiliGramos.setText(str(self.calculateMili(base)))
                    self.txtMicroGramos.setText(str(self.calculateMicro(base)))
                    self.txtNanoGramos.setText(str(self.calculateNano(base)))
            elif sender == self.txtLitros:
                base = self.txtLitros.text()
                if base.isnumeric:
                    self.txtDecaLitros.setText(str(self.calculateDeca(base)))
                    self.txtHectoLitros.setText(str(self.calculateHecto(base)))
                    self.txtKiloLitros.setText(str(self.calculateKilo(base)))
                    self.txtMegaLitros.setText(str(self.calculateMega(base)))
                    self.txtDeciLitros.setText(str(self.calculateDeci(base)))
                    self.txtCentiLitros.setText(str(self.calculateCenti(base)))
                    self.txtMiliLitros.setText(str(self.calculateMili(base)))
                    self.txtMicroLitros.setText(str(self.calculateMicro(base)))
                    self.txtNanoLitros.setText(str(self.calculateNano(base)))
        except Exception as e:
            print(e)

    def calculateDeca(self, base):
        return int(base) * (10 ** 1)

    def calculateHecto(self, base):
        return int(base) * (10 ** 2)

    def calculateKilo(self, base):
        return int(base) * (10 ** 3)

    def calculateMega(self, base):
        return int(base) * (10 ** 6)

    def calculateDeci(self, base):
        return int(base) * (10 ** -1)

    def calculateCenti(self, base):
        return int(base) * (10 ** -2)

    def calculateMili(self, base):
        return int(base) * (10 ** -3)

    def calculateMicro(self, base):
        return int(base) * (10 ** -6)

    def calculateNano(self, base):
        return int(base) * (10 ** -9)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

