import serial as conn
arduino = conn.Serial(port="com4", baudrate=9600, timeout=1)
print("Connected to Arduino")

with open('/Unidad 4/Archivos/PotenciometerData.csv', 'w') as file:
    i = 0
    while i < 10:
        a = arduino.readline()
        a = a.decode("utf-8")
        a = a.strip()
        file.write(a + '\n')
        i += 1