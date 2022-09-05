import serial, time

Serialarduino = serial.Serial('COM1', 9600)
time.sleep(1)

while True:
    edu= int(Serialarduino.readline().decode('ascii'))
    if edu = 2:
        print("sensor activado")
    if edu = 3:
        print("sensor desactivado")

