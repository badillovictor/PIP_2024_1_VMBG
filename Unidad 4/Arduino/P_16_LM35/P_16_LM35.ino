// LM35 Sensor de temperatura analogico
// Cada grado equivale a aprox 5mV
int lm35 = A0;

// ADC
// Ref. Vol: 5V
// Bits de resolucion: 10 -> 1024 valores
//  0V = 0    |   5V = 1023
// 5 / 1023 = 0.0048 Volts = 4.8mV
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(lm35);
  Serial.print(String(valor) + ",");
  valor = (5 * valor * 100) / 1023;
  Serial.println(String(valor)); 
  delay(1000);
}
