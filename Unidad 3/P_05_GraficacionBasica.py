from matplotlib import pyplot as plt
import numpy as np


def cuadraticFunction(x):
    return x ** 2


x = [i for i in range(-10, 10)]
y = [cuadraticFunction(i) for i in x]

plt.plot(x, y)
plt.show()
