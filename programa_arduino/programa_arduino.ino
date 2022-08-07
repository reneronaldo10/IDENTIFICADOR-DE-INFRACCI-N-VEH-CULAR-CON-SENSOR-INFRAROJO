// C++ code
//
int trig = 8;
int hecho = 12;
int duracion;
int distancia;
  
void setup()
{
  Serial.begin(9600);
  pinMode(trig,OUTPUT);
  pinMode(hecho,INPUT);
  
}

void loop()
{
  digitalWrite(trig, HIGH);//Codigo del sensor ultrasonico
  delayMicroseconds(1); 
  digitalWrite(trig, LOW);
  delayMicroseconds(1);
  
  duracion = pulseIn(hecho, HIGH);
  distancia = duracion/58.2;
  
  if (distancia < 45){
    Serial.println("Ha sobrepasado la linea de pare");
    delay(5000);
   }
   
   
}
