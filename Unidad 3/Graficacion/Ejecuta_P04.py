import sys
import P_00_PlantillaGrafica as Interfaz
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt


class MyApp(QtWidgets.QMainWindow, Interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnGraph.clicked.connect(self.graph)
        self.btnSet.clicked.connect(self.set_title)
        self.btnGrid.clicked.connect(self.toggle_grid)
        self.btnClear.clicked.connect(self.clear)

        # Line Style
        self.cbStyle.addItem('Estilo: :', ':')
        self.cbStyle.addItem('Estilo: -', '-')
        self.cbStyle.addItem('Estilo: --', '--')
        self.cbStyle.addItem('Estilo: -.', '-.')
        self.cbStyle.currentIndexChanged.connect(self.change_style)

        # Line Color
        self.cbColor.addItem('Negro', 'black')
        self.cbColor.addItem('Rojo', 'red')
        self.cbColor.addItem('Azul', 'blue')
        self.cbColor.addItem('Verde', 'green')
        self.cbColor.currentIndexChanged.connect(self.change_color)

        # Line Width
        self.spbWidth.setValue(1)
        self.spbWidth.setMaximum(10)
        self.spbWidth.setMinimum(1)
        self.spbWidth.setSingleStep(1)
        self.spbWidth.valueChanged.connect(self.change_width)

        # Defaults
        self.estiloLinea = ':'
        self.colorLinea = 'black'
        self.anchoLinea = 1

        self.spbXmin.setValue(0)
        self.spbXmin.setMaximum(10000)
        self.spbXmin.setMinimum(-10000)
        self.spbXmin.setSingleStep(1)
        self.spbXmin.valueChanged.connect(self.minX)

        self.spbXmax.setValue(10)
        self.spbXmax.setMaximum(10000)
        self.spbXmax.setMinimum(-10000)
        self.spbXmax.setSingleStep(1)
        self.spbXmax.valueChanged.connect(self.maxX)

        self.spbTx.setValue(10)
        self.spbTx.setMaximum(10)
        self.spbTx.setMinimum(1)
        self.spbTx.setSingleStep(1)
        self.spbTx.valueChanged.connect(self.divisionesX)

        self.spbYmin.setValue(0)
        self.spbYmin.setMaximum(10000)
        self.spbYmin.setMinimum(-10000)
        self.spbYmin.setSingleStep(1)
        self.spbYmin.valueChanged.connect(self.minY)

        self.spbYmax.setValue(10)
        self.spbYmax.setMaximum(10000)
        self.spbYmax.setMinimum(-10000)
        self.spbYmax.setSingleStep(1)
        self.spbYmax.valueChanged.connect(self.maxY)

        self.spbTy.setValue(10)
        self.spbTy.setMaximum(10)
        self.spbTy.setMinimum(1)
        self.spbTy.setSingleStep(1)
        self.spbTy.valueChanged.connect(self.divisionesY)

        self.xMax = 10
        self.xMin = 1
        self.xDivisiones = 10
        self.yMax = 10
        self.yMin = 1
        self.yDivisiones = 10

    # Área de los Slots
    def minX(self):
        self.xMin = self.spbXmin.value()
        self.clear()
        self.graph()

    def maxX(self):
        self.xMax = self.spbXmax.value()
        self.clear()
        self.graph()

    def divisionesX(self):
        self.xDivisiones = self.spbTx.value()
        self.clear()
        self.graph()

    def minY(self):
        self.yMin = self.spbYmin.value()
        self.clear()
        self.graph()

    def maxY(self):
        self.yMax = self.spbYmax.value()
        self.clear()
        self.graph()

    def divisionesY(self):
        self.yDivisiones = self.spbTy.value()
        self.clear()
        self.graph()

    def graph(self):
        try:
            polinomio = self.txtPolynom.text()
            polinomio = polinomio.replace("^", "**")

            # x = [i for i in range(-5,6)] #[-5 5]
            x = [i for i in range(self.xMin, self.xMax + 1)]
            print("Valores de X: ")
            print(x)

            # y = polinomio.replace("x","*("+str(x[0])+")")
            y = [eval(polinomio.replace("x", "*(" + str(i) + ")")) for i in x]
            print("Valores de Y: ")
            print(y)

            # self.ax.plot(x,y)
            # self.ax.plot(x, y,"g*--")
            self.ax.plot(x, y,

                         linestyle=self.estiloLinea,  #: - -- -.
                         color=self.colorLinea,  # color de la linea
                         linewidth=self.anchoLinea,  # tamaño de la linea
                         marker="x",  # o . *  x   1
                         markersize=12,
                         markerfacecolor="yellow",  # color interno del marcador
                         markeredgewidth=2,  # tamaño del borde del marcador
                         markeredgecolor="red",  # color del borde del marcador
                         dash_capstyle="butt",  # dash or solid : "butt" "round" "projecting"
                         dash_joinstyle="miter"  # dash or solid : "miter" "round" "bevel"
                         )

            # Establecer los limites
            self.ax.set_xlim(self.xMin, self.xMax + 1)
            self.ax.set_ylim(self.yMin, self.yMax + 1)

            self.ax.set_xlabel("Eje X")
            self.ax.set_ylabel("Eje Y")

            # totalelementosenX/totaldivisionesDeseadas = 8
            # mediante un ciclo se obtiene:

            # si comienzo con xmin en 0 seria:
            # xtick = [0, 10, 20, 30, 40, 50, 60, 70, 80]

            # si comienzo con xmin en n seria:

            xtick = []
            for i in range(self.xMin, self.xMax + 1, self.xDivisiones):
                xtick.append(i)
            print("Ticks para X: ")
            print(xtick)
            self.ax.set_xticks(xtick)

            ytick = []
            for i in range(self.yMin, self.yMax + 1, self.yDivisiones):
                ytick.append(i)
            print("Ticks para Y: ")
            print(ytick)
            self.ax.set_yticks(ytick)

            #self.ax.set_yticks(y)  # NOTA.. CHECK!

            # una posibilidad para establecer los ticks sería:
            # Tomar el conjunto y dividirlo entre el total de "divisiones" que el usuario desee

            self.canvas.draw()
        except Exception as e:
            print(e)

    def set_title(self):
        t = self.txtTitle.text()
        self.ax.set_title(t)  # establece el titulo
        self.canvas.draw()

    def clear(self):
        plt.cla()  # borra_todo
        self.canvas.draw()  # vuelve a dibujar

    def toggle_grid(self):
        texto = self.btnGrid.text()
        if texto == "OFF":
            self.btnGrid.setText("ON")
            plt.grid(False)
        else:
            self.btnGrid.setText("OFF")
            plt.grid(True)
        self.canvas.draw()

    def change_style(self):
        estilo = self.cbStyle.currentData()
        self.estiloLinea = estilo
        self.clear()
        self.graph()

    def change_color(self):
        color = self.cbColor.currentData()
        self.colorLinea = color
        self.clear()
        self.graph()

    def change_width(self):
        ancho = self.spbWidth.value()
        self.anchoLinea = ancho
        self.clear()
        self.graph()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
