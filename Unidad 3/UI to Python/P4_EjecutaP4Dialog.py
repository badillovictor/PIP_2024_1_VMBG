import sys
import P3_DialogResultado as interfaz
from PyQt5 import uic, QtWidgets

qtCreatorFileD = "P4_DialogSuma.ui"  # Nombre del archivo aquí.
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFileD)


class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, vPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.acceso = vPrincipal
        self.btnSumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        a = int(self.txtValorA.text())
        b = int(self.txtValorB.text())
        self.acceso.txtResultado.setText(str(a+b))
        self.close()
