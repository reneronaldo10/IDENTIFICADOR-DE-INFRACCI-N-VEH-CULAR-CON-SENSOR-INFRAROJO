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
  
  if (distancia < 100){
    Serial.println(1);
    delay(5000);
   }else
    Serial.println(0);
    delay(5000);
   
   
}
