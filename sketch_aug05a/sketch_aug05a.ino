int sensorPin = 9;
int value = 0;

void setup() {
  Serial.begin(9600);   //iniciar puerto serie
  pinMode(sensorPin , INPUT);  //definir pin como entrada
}
 
void loop(){
  value = digitalRead(sensorPin );  //lectura digital de pin
 
  if (value == LOW) {
      Serial.println(" Ha sobrepasado la linea de pare ");
  }
  delay(1000);
}
