import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P_03_ComboBoxui.ui"  # Nombre del archivo aquí.
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
        self.cmbIntegrantes.addItem('--Select--', 0)
        self.cmbIntegrantes.addItem('Victor Manuel', 1)
        self.cmbIntegrantes.addItem('Moises Heduardo', 2)
        self.cmbIntegrantes.addItem('Sofia Hernandez', 3)
        self.cmbIntegrantes.addItem('Uriel Gonzalez', 4)
        self.cmbIntegrantes.currentIndexChanged.connect(self.setData)
    # Área de los Slots
    def setData(self):
        if self.sender().currentData() == 1:
            print(
                'Nombre: \t' + self.datosIntegrantes[1][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[1][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[1][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[1][3]
            )
            self.lbImagen.setPixmap(QtGui.QPixmap(self.datosIntegrantes[1][4]))
        elif self.sender().currentData() == 2:
            print(
                'Nombre: \t' + self.datosIntegrantes[2][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[2][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[2][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[2][3]
            )
            self.lbImagen.setPixmap(QtGui.QPixmap(self.datosIntegrantes[2][4]))
        elif self.sender().currentData() == 3:
            print(
                'Nombre: \t' + self.datosIntegrantes[3][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[3][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[3][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[3][3]
            )
            self.lbImagen.setPixmap(QtGui.QPixmap(self.datosIntegrantes[3][4]))
        elif self.sender().currentData() == 4:
            print(
                'Nombre: \t' + self.datosIntegrantes[4][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[4][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[4][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[4][3]
            )
            self.lbImagen.setPixmap(QtGui.QPixmap(self.datosIntegrantes[4][4]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
