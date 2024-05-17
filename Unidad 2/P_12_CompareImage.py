import random
import sys
import time

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P_12_CompareImage.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.imageListTarget = []
        self.imageListPlayer = []
        self.targetIndex = 0
        self.playerIndex = 0
        self.changingState = False

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
            if self.targetIndex == len(self.imageListTarget) - 1:
                self.btnNext.setEnabled(False)
            self.btnPrev.setEnabled(True)
        else:
            self.targetIndex -= 1
            if self.targetIndex == 0:
                self.btnNext.setEnabled(False)
            self.btnPrev.setEnabled(True)
            pass

    def cycleImagesTimer(self):
        # Move next in imgListPlayer
        pass

    def check(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
