import serial, time
import cv2

import cloudinary
cloudinary.config( 
  cloud_name = "usidimagecloud-untg7", 
  api_key = "565111592984726", 
  api_secret = "8Tu9z0PjNxx4U2dEi1FQCzt3lk0",

)

import cloudinary.uploader
import cloudinary.api


## iniciamos con la señal del semáforo (Arduino)
    ##el programa se activa al enviar la señal de la luz roja
    

Serialarduino = serial.Serial('COM7', 9600)
time.sleep(1)
    
while True:
    cad = int(Serialarduino.readline().decode('ascii'))

    if cad == 1:
    
        cap = cv2.VideoCapture(0)
        leido, frame = cap.read()
    
        if leido == True:
            cv2.imwrite("foto.png", frame)
            
            ##Al tomar la foto, la sube a la nube
            cloudinary.uploader.upload("foto.png")
            
            print("Foto tomada correctamente y almacenada en la nube")
        
        else:
            print("Error al acceder a la cámara")
    
        cap.release()

    elif cad == 0:
        print("no se ha pasado la linea de pare")

    
   




   
