import serial, time
import cv2


Serialarduino = serial.Serial('COM7', 9600)
time.sleep(1)

cad = int(Serialarduino.readline().decode('ascii'))

if cad == 1:
    
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()
    
    if leido == True:
        cv2.imwrite("foto.png", frame)
        print("Foto tomada correctamente")
    else:
        print("Error al acceder a la cámara")
    
    cap.release()

elif cad == 0:
    print("no se ha pasado la linea de pare")
   
