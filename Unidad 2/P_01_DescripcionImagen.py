import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P_01_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.index = 1
        self.datosIntegrantes = {
            1: ['Victor Manuel Badillo Gonzalez', 'Persona', '17', 'O-', ':/Personas/YoMero.png'],
            2: ['Moises Eduardo Juarez Beltran', 'Carlotear', '20', 'A+', ':/Personas/Moy.png'],
            3: ['Sofia Hernandez Arrazola', 'Dormir', '20', 'B+', ':/Personas/Sofia.png'],
            4: ['Uriel Gonzalez Gabriel', 'Estudiar', '21', 'D-', ':/Personas/Uriel.png']
        }
        self.btnAnterior.clicked.connect(self.moveBack)
        self.btnSiguiente.clicked.connect(self.moveNext)
    # Área de los Slots
    def moveBack(self):
        if self.index == 1:
            self.index = 4
        else:
            self.index -= 1
        self.txtNombre.setText(self.datosIntegrantes[self.index][0])
        self.txtPasatiempo.setText(self.datosIntegrantes[self.index][1])
        self.txtEdad.setText(self.datosIntegrantes[self.index][2])
        self.txtSangre.setText(self.datosIntegrantes[self.index][3])
        self.lbImagen.setPixmap(QtGui.QPixmap(self.datosIntegrantes[self.index][4]))

    def moveNext(self):
        if self.index == 4:
            self.index = 1
        else:
            self.index += 1
        self.txtNombre.setText(self.datosIntegrantes[self.index][0])
        self.txtPasatiempo.setText(self.datosIntegrantes[self.index][1])
        self.txtEdad.setText(self.datosIntegrantes[self.index][2])
        self.txtSangre.setText(self.datosIntegrantes[self.index][3])
        self.lbImagen.setPixmap(QtGui.QPixmap(self.datosIntegrantes[self.index][4]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
