int ENA = 4;
int IN1 = 5;
int IN2 = 6;
int PIR = 7;
int LDR = A0;
int relevador = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10;
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(relevador, OUTPUT);
  pinMode(PIR, INPUT_PULLUP);
}

int valPIR;
int valLDR;
void loop() {
  // put your main code here, to run repeatedly:
  valPIR = digitalRead(PIR);
  if(valPIR > 100){
    int v = valPIR % 3;
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
    }
  }
  valLDR = analogRead(LDR);
  if(valLDR > 500){
    digitalWrite(relevador, valLDR);
    Serial.println("Estado Aplicado: " + String(valLDR));
  }
  delay(2000);
}
