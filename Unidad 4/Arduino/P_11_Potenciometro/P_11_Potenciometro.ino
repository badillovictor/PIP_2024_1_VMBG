// Voltaje de Referencia  => 5V 
// Bits de resolucion     => 10 bits => 1024 valores

// Cada valor del Arudino se distancia uno del otro el 4.8mV

// La señal analogica del Arduino funcionana con los pines analogicos (A#)

int potenciometro = A0; // => Pin A0

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  // pinMode no se utiliza para pines analogicos
  // Los pines analogicos son solo de entrada
}

// Potenciometro  P1    P1    P2
//                GND   A#    5V

int valorP;
void loop() {
  // put your main code here, to run repeatedly:
  valorP = analogRead(potenciometro);
  Serial.println(valorP);
  delay(100);
}