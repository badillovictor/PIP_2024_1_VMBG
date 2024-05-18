import random
import sys
import time

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P_12_CompareImage.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.imageList = [':/Personas/YoMero.png', ':/Personas/Moy.png', ':/Personas/Sofia.png', ':/Personas/Uriel.png']
        self.targetIndex = 0
        self.playerIndex = 0
        self.timerON = False

        # Área de los Signals
        self.btnSwitch.clicked.connect(self.switch)
        self.btnPrev.clicked.connect(self.cycleImages)
        self.btnNext.clicked.connect(self.cycleImages)
        self.btnCheck.clicked.connect(self.check)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.cycleImagesTimer)

    # Área de los Slots
    def cycleImages(self):
        if self.sender() == self.btnNext:
            self.targetIndex += 1
            if self.targetIndex == len(self.imageList) - 1:
                self.btnNext.setEnabled(False)
            self.btnPrev.setEnabled(True)
        else:
            self.targetIndex -= 1
            if self.targetIndex == 0:
                self.btnNext.setEnabled(False)
            self.btnPrev.setEnabled(True)
        self.lblTarget.setPixmap(QtGui.QPixmap(self.imageList[self.targetIndex]))


    def cycleImagesTimer(self):
        try:
            self.playerIndex = (self.playerIndex + 1) % len(self.imageList)
            self.lblPlayer.setPixmap(QtGui.QPixmap(self.imageList[self.playerIndex]))
        except Exception as e:
            print(e)

    def check(self):
        if self.targetIndex == self.playerIndex:
            msj = QtWidgets.QMessageBox()
            msj.setText(str('Yay'))
            msj.exec_()

    def switch(self):
        if self.timerON:
            self.timer.stop()
        else:
            self.timer.start(1000)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
