int LDR = A0;
int LED = 4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(LED, OUTPUT);
}

int valor;
void loop() {
  valor = analogRead(LDR);
  if(valor > 500){
    digitalWrite(LED, 1);
    Serial.println("LEDs Apagdos");
  } else {
    digitalWrite(LED, 0);
    Serial.println("LEDs Encendidos");
  }
  delay(200);
}
