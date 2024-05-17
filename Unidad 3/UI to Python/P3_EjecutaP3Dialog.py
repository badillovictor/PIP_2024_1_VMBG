import sys
import P3_DialogResultado as interfaz
from PyQt5 import uic, QtWidgets

qtCreatorFileD = "P3_DialogResultado.ui"  # Nombre del archivo aquí.
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFileD)


class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals

    # Área de los Slots
