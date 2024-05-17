import sys
from PyQt5 import uic, QtWidgets
import P_02_LeerArchivos as rf
qtCreatorFile = "P_03_ListaAlumnos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.todo = rf.readFile('../Unidad 3/Archivos/archivo.csv')

        # Área de los Signals
        for element in self.todo:
            self.listWidget.addItem(element[0])


    # Área de los Slots



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

