import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog

qtCreatorFile = "P_06_VerticalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datosIntegrantes = {
            1: ['Victor Manuel Badillo Gonzalez', 'Persona', '17', 'O-', ':/Personas/YoMero.png'],
            2: ['Moises Eduardo Juarez Beltran', 'Carlotear', '20', 'A+', ':/Personas/Moy.png'],
            3: ['Sofia Hernandez Arrazola', 'Dormir', '20', 'B+', ':/Personas/Sofia.png'],
            4: ['Uriel Gonzalez Gabriel', 'Estudiar', '21', 'D-', ':/Personas/Uriel.png']
        }
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(4)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.valueChanged.connect(self.setData)

    # Área de los Slots
    def setData(self):
        try:
            print(self.verticalSlider.value())
            dataKey = self.verticalSlider.value()
            print(dataKey)
            img = self.datosIntegrantes[dataKey][4]
            self.lbImagen.setPixmap(QtGui.QPixmap(img))
        except Exception as e:
            print(e)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
