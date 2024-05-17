import sys
import time

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P_08_Timer.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.cont = None
        self.num = None
        self.setupUi(self)

        # Área de los Signals
        self.btnIniciar.clicked.connect(self.iniciar)
        self.btnIniciar_2.clicked.connect(self.iniciar2)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.contar)

    # Área de los Slots
    def iniciar(self):
        n = int(self.txtNumero.text())
        print(n)
        for i in range(n):
            print("sum")
            self.lblContador.setText(str(i + 1))
            time.sleep(1)
            print(i + 1)

    def iniciar2(self):
        self.num = int(self.txtNumero_2.text())
        self.segundoPlano.start(500)
        self.cont = 1

    def contar(self):
        print('Ejecutar Contar')
        if self.cont < self.num:
            self.cont += 1
            self.lblContador.setText(str(self.cont))
        else:
            self.segundoPlano.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
