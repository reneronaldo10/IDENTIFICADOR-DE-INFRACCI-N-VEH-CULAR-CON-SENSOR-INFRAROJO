import serial, time

Serialarduino = serial.Serial('COM1', 9600)
time.sleep(1)

cad = Serialarduino.readline().decode('ascii')

if cad == 1:
    import cv2
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()
    if leido == True:
        cv2.imwrite("foto.png", frame)
        print("Foto tomada correctamente")
    else:
        print("Error al acceder a la cámara")

elif cad == 0:
    print("no se ha pasado la linea de pare")
   
cap.release()