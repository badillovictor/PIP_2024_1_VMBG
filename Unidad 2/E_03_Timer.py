import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E_03_Timer.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.seconds = 0

        # Área de los Signals
        self.btnStart.clicked.connect(self.startTimerCustom)
        self.secondPlane = QtCore.QTimer()
        self.secondPlane.timeout.connect(self.tick)

    # Área de los Slots
    def startTimerCustom(self):
        self.seconds = int(self.txtTimer.text())
        self.lcdTimer.display(self.seconds)
        self.secondPlane.start(1000)

    def tick(self):
        print(self.seconds)
        if self.seconds != 0:
            self.seconds -= 1
            self.lcdTimer.display(self.seconds)
        else:
            self.secondPlane.stop()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Its over')
            msgBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

