import sys
import P_00_PlantillaGrafica as Interfaz
from PyQt5 import QtWidgets


class MyApp(QtWidgets.QMainWindow, Interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

    # Área de los Slots


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
