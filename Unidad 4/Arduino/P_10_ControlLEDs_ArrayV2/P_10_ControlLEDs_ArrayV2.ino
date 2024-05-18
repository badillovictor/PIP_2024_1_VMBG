int led[] = {
  2, 3, 4, 5, 6, 7, 8, 9
};
int ledStates[] = {
  false, false, false, false, false, false, false, false
};

void setup() {
  // put your setup code here, to run once:
  for(int = 0; i<8; i++){
    pinMode(led[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(15);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int ledIndex = Serial.readString().toInt() - 1;
    ledStates[ledIndex] = !ledStates[ledIndex];
    digitalWrite(led[ledIndex], ledStates[ledIndex]);
  }
  delay(200);
}