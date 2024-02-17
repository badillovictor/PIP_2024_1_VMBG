import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P_02_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.index = 1
        self.datosIntegrantes = {
            1: ['Victor Manuel Badillo Gonzalez', 'Persona', '17', 'O-', ':/Fotos/ruta.png'],
            2: ['Moises Eduardo Juarez Beltran', 'Carlotear', '20', 'A+', ':/Fotos/ruta.png'],
            3: ['Sofia Hernandez Arrazola', 'Dormir', '20', 'B+', ':/Fotos/ruta.png'],
            4: ['Uriel Gonzalez Gabriel', 'Estudiar', '21', 'D-', ':/Fotos/ruta.png']
        }
        self.cbxIntegrante1.clicked.connect(self.setData)
        self.cbxIntegrante2.clicked.connect(self.setData)
        self.cbxIntegrante3.clicked.connect(self.setData)
        self.cbxIntegrante4.clicked.connect(self.setData)
    # Área de los Slots
    def setData(self):
        if self.sender() == self.cbxIntegrante1:
            self.txtDatos.setText(
                'Nombre: \t' + self.datosIntegrantes[1][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[1][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[1][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[1][3]
            )
            self.cbxIntegrante2.setCheckState(False)
            self.cbxIntegrante3.setCheckState(False)
            self.cbxIntegrante4.setCheckState(False)
        elif self.sender() == self.cbxIntegrante2:
            self.txtDatos.setText(
                'Nombre: \t' + self.datosIntegrantes[2][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[2][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[2][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[2][3]
            )
            self.cbxIntegrante1.setCheckState(False)
            self.cbxIntegrante3.setCheckState(False)
            self.cbxIntegrante4.setCheckState(False)
        elif self.sender() == self.cbxIntegrante3:
            self.txtDatos.setText(
                'Nombre: \t' + self.datosIntegrantes[3][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[3][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[3][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[3][3]
            )
            self.cbxIntegrante1.setCheckState(False)
            self.cbxIntegrante2.setCheckState(False)
            self.cbxIntegrante4.setCheckState(False)
        elif self.sender() == self.cbxIntegrante4:
            self.txtDatos.setText(
                'Nombre: \t' + self.datosIntegrantes[4][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[4][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[4][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[4][3]
            )
            self.cbxIntegrante1.setCheckState(False)
            self.cbxIntegrante2.setCheckState(False)
            self.cbxIntegrante3.setCheckState(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
