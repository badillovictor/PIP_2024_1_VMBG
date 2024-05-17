int led = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(led, OUTPUT);
}

int val;
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    val = Serial.readString().toInt();
    digitalWrite(led, val);
    if(val == 1){
      Serial.println("LED Prendido");
    } else {
      Serial.println("LED Apagado");
    }
  }
}
