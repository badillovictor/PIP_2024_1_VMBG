from matplotlib import pyplot as plt
import serial as conn

arduino = conn.Serial(port="COM3", baudrate=9600, timeout=1)
print('Connected to Arduino')
x = [i for i in range(100)]
y = [0 for i in range(100)]
i = 0

while True:
    a = arduino.readline().decode().strip()
    y.pop(0)
    y.append(int(a))
    print(y)
    plt.plot(x, y)
    plt.grid = True
    plt.show()

