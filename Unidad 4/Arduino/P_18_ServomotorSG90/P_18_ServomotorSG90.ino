#include "Servo.h"   

int pinServo = 9;
Servo servo; 

void setup(){ 
  Serial.begin(9600);
  servo.attach(pinServo);
}
 
void loop(){
  if(Serial.available() > 0){
    int x = Serial.readString().toInt();
    servo.write(x);
  }
}
