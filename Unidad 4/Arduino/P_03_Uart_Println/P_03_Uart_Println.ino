
void setup() {
  // put your setup code here, to run once:
  //Modulo UART  --Universal Asycronic Data Receipt and Transmision Module---
  Serial.begin(9600); //Inicializa la comunicacion serial
  //9600 baudios a los que se comunica arduino con otros dispositivos

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hola! :D! <3");
  delay(500); //miliseconds
}
