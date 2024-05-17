import serial as conn
arduino = conn.Serial(port="com4", baudrate=9600, timeout=1)
print("Connected to Arduino")

while True:
    a = arduino.readline()
    a = a.decode()
    a = a.strip()
    print(a)