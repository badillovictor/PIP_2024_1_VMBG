//El arudino tiene un led interno en el pin digital 13
int led = 13;
//Arduino UNO tiene 0-13 pines
  //Cuenado se utiliza comuc. serial no se puede usar los pines 0 y 1

//Arduino MEGA tiene 55 pines

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, HIGH);
  Serial.println("LED vivido");
  delay(1000);
  digitalWrite(led, LOW);
  Serial.println("LED morido");
  delay(1000);
}
