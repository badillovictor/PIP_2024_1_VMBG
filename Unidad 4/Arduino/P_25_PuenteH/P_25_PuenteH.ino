/*
l298 - 2 puentes H
.                                                           Arduino                Motor
ENA         ENB        - Velocidad de giro   (0-255)                ┌─────────┐
IN1         IN3        - Sentido de giro                     IN1  ─ │         │ ─  OUT1
IN2         IN4                                                     │         │
OUT1        OUT3                                             IN2  ─ │         │ ─  OUT2
OUT2        OUT4                                                    └─────────┘
.                                                                        │
IN1       IN2                                                           EnA
 1         1    Aniquilacion total de todo lo que existe equivalente al consumo del unvierso entero por antimateria
 0         0    Detenerse
 0         1    Hacia un lado
 1         0    Pal otro


*/

int ENA = 4; //Pin PWM
int IN1 = 5;
int IN2 = 6;
// OUT1 / 2 se conectan directamente del puente H al circuito externo

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int v = Serial.readString().toInt();
    if (v == 0) {
      Serial.println("Detenerse");
      digitalWrite(IN1, 0);
      digitalWrite(IN2, 0);
      analogWrite(ENA, 0);
    } else if (v == 1) {
      Serial.println("Girar Izquierda");
      digitalWrite(IN1, 0);
      digitalWrite(IN2, 1);
      analogWrite(ENA, 255);
    } else if (v == 2) {
      Serial.println("Girar Derecha");
      digitalWrite(IN1, 1);
      digitalWrite(IN2, 0);
      analogWrite(ENA, 255);
    } else {
      Serial.println("Movimiento no valido");
    }
  }
  delay(100);
}
