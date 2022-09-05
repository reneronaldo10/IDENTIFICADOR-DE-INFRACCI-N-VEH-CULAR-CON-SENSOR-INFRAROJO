
import serial, time

Serialarduino = serial.Serial('COM5', 9600)
time.sleep(1)

while True:
    cad = Serialarduino.readline().decode('ascii')
    print(cad) 

