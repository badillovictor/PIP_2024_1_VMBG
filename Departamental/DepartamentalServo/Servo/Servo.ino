#include "Servo.h"   

int pinServo = 9;
int PIR = 4;
Servo servo; 

void setup(){ 
  Serial.begin(9600);
  Serial.setTimeout(10);
  servo.attach(pinServo);
  pinMode(PIR, INPUT_PULLUP);
}
 
int val;
void loop(){
  val = digitalRead(PIR);
  if(val > 100){
    servo.write(val);
    Serial.println("Movimiento Detectado...Moviendo Servo");
    delay(2000);
    Serial.println("Esperando Movimiento...")
  }
  delay(1000)
}
