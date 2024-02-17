import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P_04_Dialui.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datosIntegrantes = {
            1: ['Victor Manuel Badillo Gonzalez', 'Persona', '17', 'O-', ':/Fotos/ruta.png'],
            2: ['Moises Eduardo Juarez Beltran', 'Carlotear', '20', 'A+', ':/Fotos/ruta.png'],
            3: ['Sofia Hernandez Arrazola', 'Dormir', '20', 'B+', ':/Fotos/ruta.png'],
            4: ['Uriel Gonzalez Gabriel', 'Estudiar', '21', 'D-', ':/Fotos/ruta.png']
        }
        self.dialIntegrantes.setMinimum = 1
        self.dialIntegrantes.setMaximum = 100
        self.dialIntegrantes.setStep = 1
        self.dialIntegrantes.value = 1
        self.dialIntegrantes.valueChanged.connect(self.setData)

    # Área de los Slots
    def setData(self):
        try:
            print(self.dialIntegrantes.value)
        except Exception as e:
            print(e)
        '''
        if self.sender().value() == 1:
            print(
                'Nombre: \t' + self.datosIntegrantes[1][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[1][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[1][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[1][3]
            )
        elif self.sender().value() == 2:
            print(
                'Nombre: \t' + self.datosIntegrantes[2][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[2][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[2][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[2][3]
            )
        elif self.sender().value() == 3:
            print(
                'Nombre: \t' + self.datosIntegrantes[3][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[3][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[3][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[3][3]
            )
        elif self.sender().value() == 4:
            print(
                'Nombre: \t' + self.datosIntegrantes[4][0] + '\n' +
                'Pasatiempo: \t' + self.datosIntegrantes[4][1] + '\n' +
                'Edad: \t' + self.datosIntegrantes[4][2] + '\n' +
                'Tipo Sangre: \t' + self.datosIntegrantes[4][3]
            )
        '''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
