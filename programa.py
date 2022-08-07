import serial, time

Serialarduino = serial.Serial('COM4', 9600)
time.sleep(1)

cad = Serialarduino.readline().decode('ascii')
if cad = 1:
