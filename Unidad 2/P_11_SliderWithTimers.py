import random
import sys
import time

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P_11_SliderWithTimers.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnIniciar.clicked.connect(self.switch)
        self.secondPlane = QtCore.QTimer()
        self.secondPlane.timeout.connect(self.goAround)

    # Área de los Slots
    def switch(self):
        t = self.btnIniciar.text()
        if t == 'INICIAR':
            self.btnIniciar.setText('DETENER')
            self.secondPlane.start(500)
        else:
            self.btnIniciar.setText('INICIAR')
            self.secondPlane.stop()
            if self.lblImagen.text() == 'Pranked!':
                messageBox = QtWidgets.QMessageBox()
                messageBox.setText('You WON!')
                messageBox.exec_()

    def goAround(self):
        '''
        Make a list of all images routes
        Find a way to move around the list
        Change label pixmap to circle through the list
        Buy quesadillas
        Eat said quesadillas
        '''
        i = random.randint(0, 100)
        if i >= 50:
            self.lblImagen.setText('...')
        elif i >= 30:
            self.lblImagen.setText('Ranked!')
        elif i >= 20:
            self.lblImagen.setText('Franked!')
        elif i >= 10:
            self.lblImagen.setText('Cranked!')
        elif i >= 5:
            self.lblImagen.setText('Shanked!')
        else:
            self.lblImagen.setText('Pranked!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
